#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.
"""
WIP: A Python wrapper for Brandons RemoteInput/Reflection for OSRS

Resources:
    Definitions of functions from headers:
        https://gist.github.com/Brandon-T/530ffc8780920dc12919af8d15ebac3f
    Hex code constants:
        https://gist.github.com/kkusch/245bb80ec4e7ab4d8cdc6b7eeb3f330f#file-hex_keycodes-py
    ctypes:
        https://docs.python.org/3/library/ct.html

"""
import atexit
import ctypes as ct
from typing import Tuple, List
import time

import psutil

from pyautoeios.hooks import THook
from pyautoeios.eios_meta import EIOSMetaClass, EIOSPtr, JObject, JArray, Type

CLIENTS = ["JagexLauncher.exe", "RuneLite.exe", "OpenOSRS.exe"]

SIZE = Type("size", -1, ct.c_size_t, ct.sizeof(ct.c_size_t))
CHAR = Type("char", 0, ct.c_char, ct.sizeof(ct.c_char))
BYTE = Type("byte", 1, ct.c_byte, ct.sizeof(ct.c_byte))
BOOL = Type("boolean", 2, ct.c_bool, ct.sizeof(ct.c_bool))
SHORT = Type("short", 3, ct.c_short, ct.sizeof(ct.c_short))
INT = Type("int", 4, ct.c_int, ct.sizeof(ct.c_int))
LONG = Type("long", 5, ct.c_long, ct.sizeof(ct.c_long))
FLOAT = Type("float", 6, ct.c_float, ct.sizeof(ct.c_float))
DOUBLE = Type("double", 7, ct.c_double, ct.sizeof(ct.c_double))
STRING = Type("string", 8, ct.c_void_p, ct.sizeof(ct.c_void_p))
OBJECT = Type("object", 9, ct.c_void_p, ct.sizeof(ct.c_void_p))

ALL = [CHAR, BYTE, BOOL, SHORT, INT, LONG, FLOAT, DOUBLE, STRING, OBJECT]


class EIOS(object, metaclass=EIOSMetaClass):
    """Class to wrap the remoteinput methods."""

    _clients = {}
    """Classvariable to hold the list of clients PIDS and their EIOS pointers."""

    _objects = {}
    """Classvariable to track all object pointers, so they can be free'd."""

    def __enter__(self):
        return self

    def __init__(self, pid=None):
        atexit.register(self._cleanup)
        self._eios_ptr = None
        """Pointer for the EIOS binding to the DLL."""

        self._pid = None
        """Pid for the rs client."""

        # if an explict pid wasn't passed, find the first pid, that isn't
        # already bound to a client. assume any pid
        # not alreadyu in our class variable as an "unbound" pid.
        if not pid:
            pids = self._get_client_pids()
            for _pid in pids:
                if _pid not in self._clients.keys():
                    pid = _pid
                    break
            if pid is None:
                raise IOError(f"All {len(pids)} clients already bound to.")

        # if an explict pid is passed, still check for it.
        elif pid in self._clients.keys():
            raise IOError("That Client is already paired")

        self._pid = pid
        EIOS._eios_inject_pid(pid)
        self._eios_ptr = EIOS._eios_pair_client(pid)
        if self._eios_ptr == 0:
            raise IOError("Couldn't find an available client.")

        self._clients[pid] = self._eios_ptr
        self._objects[pid] = {}
        """An individual dict for just this client's object pointers"""

    @staticmethod
    def _get_client_pids() -> List[int]:
        return [
            process.info["pid"]
            for process in psutil.process_iter(["pid", "name"])
            if process.info["name"] in CLIENTS
        ]

    def _cleanup(self):
        """Free object pointers during garbage collection.

        We track each object we reflect when the object is created.
            Although each object *should* free itself when it leave scope
            with the RSTRype.__del__, we add an extra one here at the EIOS
            level to catch any that left hanging, such as is the case with
            circular references. in normal execution, the EIOS will always
            clear, so its the last stand against memory leaks.
        """
        # print(f"{self = } , {self._pid = } , {self._eios_ptr = }")
        if self._pid:
            # print(f"unpairing client {self = }")
            if self._pid in self._objects:
                keys = self._objects.pop(self._pid).keys()
                for ref in keys:
                    self.release_object(ref)
                self._clients.pop(self._pid)

            if self.get_eios(self._pid):
                self.release_target()
                time.sleep(1)

        self._pid = None

    def __del__(self):
        self._cleanup()

    def __exit__(self, *exc):
        self._cleanup()

    def __str__(self):
        """Simple string repreentation."""
        return f"EIOS({self._pid})->({self._eios_ptr})"

    def __repr__(self):
        """Simple string repreentation."""
        return f"EIOS({self._pid})->({self._eios_ptr})"

    # @staticmethod
    # def request_target(initstr: str) -> EIOSPtr:
    #     """Wrap EIOS_RequestTarget."""
    #     return EIOS._eios_request_target(bytes(initstr, encoding="utf8"))

    def release_target(self) -> None:
        """Wrap EIOS_ReleaseTarget."""
        EIOS._eios_release_target(self._eios_ptr)

    def get_target_dimensions(self) -> Tuple[int, int]:
        """Wrap EIOS_GetTargetDimensions."""
        width = ct.c_int32()
        height = ct.c_int32()
        EIOS._eios_get_target_dimensions(
            self._eios_ptr, ct.byref(width), ct.byref(height)
        )
        return (width.value, height.value)

    def get_image_buffer(self):
        """Wrap EIOS_GetImageBuffer."""
        buffer = EIOS._eios_get_image_buffer(self._eios_ptr)
        return buffer

    def get_debug_image_buffer(self):
        """Wrap EIOS_GetDebugImageBuffer."""
        buffer = EIOS._eios_get_debug_image_buffer(self._eios_ptr)
        return buffer

    def set_graphics_debugging(self, enabled: bool):
        """Wrap EIOS_SetGraphicsDebugging."""
        EIOS._eios_set_graphics_debugging(self._eios_ptr, enabled)

    def update_image_buffer(self) -> None:
        """Wrap EIOS_UpdateImageBuffer."""
        EIOS._eios_update_image_buffer(self._eios_ptr)

    def has_focus(self) -> bool:
        """Wrap EIOS_HasFocus."""
        return EIOS._eios_has_focus(self._eios_ptr)

    def gain_focus(self) -> None:
        """Wrap EIOS_GainFocus."""
        EIOS._eios_gain_focus(self._eios_ptr)

    def lose_focus(self) -> None:
        """Wrap EIOS_LoseFocus."""
        EIOS._eios_lose_focus(self._eios_ptr)

    def is_input_enabled(self) -> bool:
        """Wrap EIOS_IsInputEnabled."""
        return EIOS._eios_is_input_enabled(self._eios_ptr)

    def set_input_enabled(self, enabled: bool) -> None:
        """Wrap EIOS_SetInputEnabled."""
        EIOS._eios_set_input_enabled(self._eios_ptr, enabled)

    def get_mouse_position(self) -> Tuple[int, int]:
        """Wrap EIOS_GetMousePosition."""
        x = ct.c_int32()
        y = ct.c_int32()
        EIOS._eios_get_mouse_position(self._eios_ptr, ct.byref(x), ct.byref(y))
        return (x.value, y.value)

    def get_real_mouse_position(self) -> Tuple[int, int]:
        """Wrap EIOS_GetRealMousePosition."""
        x = ct.c_int32()
        y = ct.c_int32()
        EIOS._eios_get_real_mouse_position(self._eios_ptr, ct.byref(x), ct.byref(y))
        return (x.value, y.value)

    def move_mouse(self, x: int, y: int) -> None:
        """Wrap EIOS_MoveMouse."""
        EIOS._eios_move_mouse(self._eios_ptr, x, y)

    def hold_mouse(self, x: int, y: int, button: int) -> None:
        """Wrap EIOS_HoldMouse."""
        EIOS._eios_hold_mouse(self._eios_ptr, x, y, button)

    def release_mouse(self, x: int, y: int, button: int) -> None:
        """Wrap EIOS_ReleaseMouse."""
        EIOS._eios_release_mouse(self._eios_ptr, x, y, button)

    def scroll_mouse(self, x: int, y: int, lines: int) -> None:
        """Wrap EIOS_ScrollMouse."""
        EIOS._eios_scroll_mouse(self._eios_ptr, x, y, lines)

    def is_mouse_button_held(self, button: int) -> bool:
        """Wrap EIOS_IsMouseButtonHeld. Not Implemented."""
        raise NotImplementedError(
            "EIOS_IsMouseButtonHeld appears to be missing from the DLL"
        )

    def send_string(self, text: str, keywait: int, keymodwait: int) -> None:
        """Wrap EIOS_SendString."""
        _text = bytes(text, encoding="utf8")
        EIOS._eios_send_string(self._eios_ptr, _text, keywait, keymodwait)

    def hold_key(self, key: int) -> None:
        """Wrap EIOS_HoldKey."""
        EIOS._eios_hold_key(self._eios_ptr, key)

    def release_key(self, key: int) -> None:
        """Wrap EIOS_ReleaseKey."""
        EIOS._eios_release_key(self._eios_ptr, key)

    def is_key_held(self, key: int) -> bool:
        """Wrap EIOS_IsKeyHeld."""
        return EIOS._eios_is_key_held(self._eios_ptr, key)

    def get_keyboard_speed(self) -> int:
        """Wrap EIOS_GetKeyboardSpeed."""
        return EIOS._eios_get_keyboard_speed(self._eios_ptr)

    def set_keyboard_speed(self, speed: int) -> None:
        """Wrap EIOS_SetKeyboardSpeed."""
        EIOS._eios_set_keyboard_speed(self._eios_ptr, speed)

    def get_keyboard_repeat_delay(self) -> int:
        """Wrap EIOS_GetKeyboardRepeatDelay."""
        return EIOS._eios_get_keyboard_repeat_delay(self._eios_ptr)

    def set_keyboard_repeat_delay(self, delay: int) -> None:
        """Wrap EIOS_SetKeyboardRepeatDelay."""
        EIOS._eios_set_keyboard_repeat_delay(self._eios_ptr, delay)

    @staticmethod
    def pair_client(pid: int) -> EIOSPtr:
        """Wrap EIOS_PairClient."""
        return EIOS._eios_pair_client(pid)

    @staticmethod
    def kill_client_pid(pid: int) -> None:
        """Wrap EIOS_KillClientPID."""
        EIOS._eios_kill_client_pid(pid)

    def kill_client(self) -> None:
        """Wrap EIOS_KillClient."""
        EIOS._eios_kill_client(self._eios_ptr)

    @staticmethod
    def kill_zombie_clients() -> None:
        """Wrap EIOS_KillZombieClients."""
        EIOS._eios_kill_zombie_clients()

    @staticmethod
    def get_clients(unpaired_only: bool = False) -> int:
        """Wrap EIOS_GetClients."""
        return EIOS._eios_get_clients(unpaired_only)

    @staticmethod
    def get_client_pid(index: int) -> int:
        """Wrap EIOS_GetClientPID."""
        return EIOS._eios_get_client_pid(index)

    @staticmethod
    def inject(process_name: str = "JagexLauncher.exe") -> None:
        """Wrap EIOS_Inject."""
        EIOS._eios_inject(process_name.encode("utf8"))

    @staticmethod
    def inject_pid(pid: int) -> None:
        """Wrap EIOS_Inject_PID."""
        EIOS._eios_inject_pid(pid)

    @staticmethod
    def get_eios(pid: int) -> EIOSPtr:
        """Wrap Reflect_GetEIOS."""
        return EIOS._reflect_get_eios(pid)

    def get_object(self, jobject: JObject, hook: THook):
        """Wrap Reflect_Object."""
        return EIOS._reflect_object(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def is_same_object(self, first: JObject, second: JObject) -> bool:
        """Wrap Reflect_IsSame_Object."""
        return EIOS._reflect_is_same_object(self._eios_ptr, first, second)

    def instance_of(self, jobject: JObject, cls_name: str):
        """Wrap Reflect_InstanceOf."""
        return EIOS._reflect_instance_of(self._eios_ptr, jobject, cls_name)

    def release_object(self, jobject: JObject):
        """Wrap Reflect_Release_Object."""
        # print(f"releasing {jobject = } from {self._eios_ptr = }")
        EIOS._reflect_release_object(self._eios_ptr, jobject)

    def release_objects(self, objects: JArray):
        """Wrap Reflect_Release_Objects."""
        size = len(objects)
        ptr = ct.cast((ct.c_void_p * size)(*objects), ct.POINTER(ct.c_void_p))
        EIOS._reflect_release_objects(self._eios_ptr, ptr, size)

    def get_bool(self, jobject: JObject, hook: THook) -> bool:
        """Wrap Reflect_Bool."""
        return EIOS._reflect_bool(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def get_char(self, jobject: JObject, hook: THook) -> bytes:
        """Wrap Reflect_Char."""
        return EIOS._reflect_char(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def get_byte(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Byte."""
        value = EIOS._reflect_byte(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 7) % 2 ** 8 - 2 ** 7

    def get_short(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Short."""
        value = EIOS._reflect_short(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 15) % 2 ** 16 - 2 ** 15

    def get_int(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Int."""
        value = EIOS._reflect_int(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 31) % 2 ** 32 - 2 ** 31

    def get_long(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Long."""
        value = EIOS._reflect_long(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 63) % 2 ** 64 - 2 ** 63

    def get_float(self, jobject: JObject, hook: THook) -> float:
        """Wrap Reflect_Float."""
        return EIOS._reflect_float(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def get_double(self, jobject: JObject, hook: THook) -> float:
        """Wrap Reflect_Double."""
        return EIOS._reflect_double(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def get_string(self, jobject: JObject, hook: THook, max_size=100):
        """Wrap Reflect_String."""
        _buffer = ct.create_string_buffer(1024)
        EIOS._reflect_string(
            self._eios_ptr,
            jobject,
            hook.cls,
            hook.field,
            hook.desc,
            _buffer,
            len(_buffer),
        )
        return _buffer.value.decode("utf8")

    def get_array(self, jobject: JObject, hook: THook):
        """Wrap Reflect_Array."""
        return EIOS._reflect_array(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def get_array_with_size(self, jobject: JObject, hook: THook):
        """Wrap Reflect_Array_With_Size."""
        size = ct.c_size_t()
        _ref = EIOS._reflect_array_with_size(
            self._eios_ptr,
            jobject,
            ct.byref(size),
            hook.cls,
            hook.field,
            hook.desc,
        )
        return (_ref, size.value)

    def get_array_size(self, jarray: JArray):
        """Wrap Reflect_Array_Size."""
        return EIOS._reflect_array_size(self._eios_ptr, jarray)

    def get_array_from_pointer(self, instance, arr_type, index, size):
        buffer_addr = EIOS._reflect_array_index(
            self._eios_ptr, instance, arr_type.value, index, size
        )

        if arr_type == STRING:
            result = [None] * size
            for i in range(size):
                string_size = ct.c_size_t.from_address(buffer_addr).value
                buffer_addr += SIZE.csize
                value = None
                if string_size > 0:
                    value = ct.c_char_p(buffer_addr).value.decode("utf8")
                    buffer_addr += string_size + 1
                result[i] = value
            return result

        data = (arr_type.ctype * size).from_address(buffer_addr)
        return data

    def get_array_index_from_pointer(self, instance, arr_type, index):
        buffer_addr = EIOS._reflect_array_index(
            self._eios_ptr, instance, arr_type.value, index, 1
        )

        if arr_type == STRING:
            _string_size = ct.c_size_t.from_address(buffer_addr).value
            # print(f"{_string_size =}")
            _value = None
            if _string_size > 0:
                _value2 = ct.c_char_p(buffer_addr + SIZE.csize).value.decode("utf8")
                _value = (
                    ct.string_at(buffer_addr + SIZE.csize, _string_size)
                    .replace(b"\xc2\xa0", b" ")
                    .decode("utf8")
                )
                if _value != _value2:
                    print(f"DEBUG: missmatch in eios.EIOS.get_array_index_from_pointer... {_value = }, {_value2 = }")
            return _value

        if arr_type == OBJECT:
            _pointer_obj = ct.cast(buffer_addr, ct.POINTER(arr_type.ctype))
            return _pointer_obj.contents.value

        data = arr_type.ctype.from_address(buffer_addr)
        if arr_type in [INT]:
            return data.value

        return data

    def get_2d_array_index_from_pointer(self, instance, arr_type, x, y):
        buffer_addr = EIOS._reflect_array_index2d(
            self._eios_ptr, instance, arr_type.value, 1, x, y
        )

        if arr_type == STRING:
            string_size = ct.c_size_t.from_address(buffer_addr).value
            value = None
            if string_size > 0:
                value = ct.c_char_p(buffer_addr + SIZE.csize).value.decode("utf8")
            return value

        data = arr_type.ctype.from_address(buffer_addr)
        return data

    def get_3d_array_index_from_pointer(self, instance, arr_type, x, y, z):
        buffer_addr = EIOS._reflect_array_index3d(
            self._eios_ptr, instance, arr_type.value, 1, x, y, z
        )

        if arr_type == STRING:
            string_size = ct.c_size_t.from_address(buffer_addr).value
            value = None
            if string_size > 0:
                value = ct.c_char_p(buffer_addr + SIZE.csize).value.decode("utf8")
            return value

        data = arr_type.ctype.from_address(buffer_addr)
        return data

    def get_4d_array_index_from_pointer(self, instance, arr_type, x, y, z, w):
        buffer_addr = EIOS._reflect_array_index4d(
            self._eios_ptr, instance, arr_type.value, 1, x, y, z, w
        )

        if arr_type == STRING:
            string_size = ct.c_size_t.from_address(buffer_addr).value
            value = None
            if string_size > 0:
                value = ct.c_char_p(buffer_addr + SIZE.csize).value.decode("utf8")
            return value

        data = arr_type.ctype.from_address(buffer_addr)
        return data

    def get_array_indices(
        self,
        jarray: JArray,
        arr_type: Type,
        indices: List[int],
    ):
        """Wrap Reflect_Array_Indices."""
        c_array_type = ct.c_int * len(indices)
        c_array = c_array_type(*indices)
        return EIOS._reflect_array_indices(
            self._eios_ptr, jarray, arr_type.value, c_array, len(indices)
        )

    # def get_array_index(
    #     self,
    #     jarray: JArray,
    #     arr_type: int,
    #     index: int,
    #     length: int,
    # ):
    #     """Wrap Reflect_Array_Index."""
    #     return EIOS._reflect_array_index(
    #         self._eios_ptr, jarray, arr_type.value, index, length
    #     )

    # def get_array_index2d(
    #     self, jarray: JArray, arr_type: int, length: int, x: int, y: int
    # ):
    #     """Wrap Reflect_Array_Index2D."""
    #     return EIOS._reflect_array_index2d(
    #         self._eios_ptr, jarray, arr_type.value, length, x, y
    #     )

    # def get_array_index3d(
    #     self,
    #     jarray: JArray,
    #     arr_type: int,
    #     length: int,
    #     x: int,
    #     y: int,
    #     z: int,
    # ):
    #     """Wrap Reflect_Array_Index3D."""
    #     return EIOS._reflect_array_index3d(
    #         self._eios_ptr, jarray, arr_type.value, length, x, y, z
    #     )

    # def get_array_index4d(
    #     self,
    #     jarray: JArray,
    #     arr_type: int,
    #     length: int,
    #     x: int,
    #     y: int,
    #     z: int,
    #     w: int,
    # ):
    #     """Wrap Reflect_Array_Index4D."""
    #     return EIOS._reflect_array_index4d(
    #         self._eios_ptr, jarray, arr_type.value, length, x, y, z, w
    #     )
