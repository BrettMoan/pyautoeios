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
"""Meta class for EIOS that sets all the C libary wrappers."""
import ctypes as ct
from dataclasses import dataclass
import pathlib
import platform
from typing import Callable, Any

try:
    from importlib.resources import files

    _LIB_DIR = files(__package__) / "lib"
except ImportError:
    import pkg_resources

    _LIB_DIR = pathlib.Path(pkg_resources.resource_filename(__package__, "lib"))


EIOSPtr = ct.c_void_p
IntPtr = ct.POINTER(ct.c_int32)
JObject = ct.c_void_p
JArray = ct.c_void_p
ClientOffset = ct.c_int
PID = ct.c_int
KeyCode = ct.c_int32
Coordinate = ct.c_int32
MouseButton = ct.c_int32


# pylint: disable=too-few-public-methods
class CStr:
    """Simple wrapper for str vs bytes for C calls."""

    @classmethod
    def from_param(cls, value):
        """Called ctypes before calling the dll function."""
        if isinstance(value, bytes):
            return value
        return value.encode("utf8")


@dataclass(frozen=True)
class Type:
    __slots__ = ["name", "value", "ctype", "csize"]
    name: str
    value: int
    ctype: Any
    csize: int


# pylint: disable=too-few-public-methods
class _type:
    """Simple wrapper for  for C calls."""

    @classmethod
    def from_param(cls, param):
        """Called ctypes before calling the dll function."""
        if isinstance(param, Type):
            return ct.c_int(param.value)
        return ct.c_int(param)


def _get_system():
    system = platform.system().lower()
    if system.startswith("linux"):
        return "linux"
    if system.startswith(("win", "cygwin")):
        return "win"
    if system.startswith(("darwin", "mac")):
        return "mac"
    raise RuntimeError('Invalid system "%s"' % system)


def _get_py_bits() -> int:
    return ct.sizeof(ct.c_voidp) * 8


def _get_py_arch() -> str:
    return (
        "arm" if any((s in platform.machine()) for s in ("arm", "aarch")) else "intel"
    )


def _get_lib_path() -> str:
    system, arch, bits = _get_system(), _get_py_arch(), _get_py_bits()
    if system == "win":
        if bits == 64:
            name = "libRemoteInput-x86_64.dll"
        else:
            name = "libRemoteInput-i686.dll"
    elif system == "mac":
        name = "libRemoteInput-x86-64.dylib"
    elif system == "linux":
        if arch == "arm":
            name = "libRemoteInput.so-arm64"
        else:
            name = "libRemoteInput.so-x86_64"
    else:
        raise RuntimeError('No valid lib for "%s-%s-%s"' % (system, arch, bits))
    return str(pathlib.Path(_LIB_DIR, name))


class EIOSMetaClass(type):
    """Meta Class for EIOS which contains static values."""

    _file = _get_lib_path()
    _cdll = ct.CDLL(_file)
    if _get_system() == "win":
        _windll = ct.WinDLL(_file)
    else:
        _windll = _cdll

    @property
    def dll_file(cls):
        return cls._file

    @property
    def cdll(cls):
        """Loading of the remote_input libraries with CDLL

        methods from `Plugin.hxx` uses wdll (windows only)
        methods from `EIOS.hxx` uses cdll (all platforms)
        """
        return cls._cdll

    @property
    def wdll(cls):
        """Loading of the remote_input libraries with CDLL

        methods from `Plugin.hxx` uses wdll (windows only)
        methods from `EIOS.hxx` uses cdll (all platforms)
        """
        return cls._windll

    @property
    def _eios_request_target(cls) -> Callable:
        """EIOS* EIOS_RequestTarget(const char* initargs) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_RequestTarget")
        fn.restype = EIOSPtr
        fn.argtypes = [CStr]
        return fn

    @property
    def _eios_release_target(cls) -> Callable:
        """void EIOS_ReleaseTarget(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_ReleaseTarget")
        fn.restype = None
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_get_target_dimensions(cls) -> Callable:
        """void EIOS_GetTargetDimensions(EIOS* eios, std::int32_t* width, std::int32_t* height) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetTargetDimensions")
        fn.restype = None
        fn.argtypes = [EIOSPtr, IntPtr, IntPtr]
        return fn

    @property
    def _eios_get_image_buffer(cls) -> Callable:
        """std::uint8_t* EIOS_GetImageBuffer(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetImageBuffer")
        fn.restype = ct.POINTER(ct.c_uint8)
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_get_debug_image_buffer(cls) -> Callable:
        """std::uint8_t* EIOS_GetDebugImageBuffer(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetDebugImageBuffer")
        fn.restype = ct.POINTER(ct.c_uint8)
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_set_graphics_debugging(cls) -> Callable:
        """void EIOS_SetGraphicsDebugging(EIOS* eios, bool enabled) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_SetGraphicsDebugging")
        fn.restype = None
        fn.argtypes = [EIOSPtr, ct.c_bool]
        return fn

    @property
    def _eios_update_image_buffer(cls) -> Callable:
        """void EIOS_UpdateImageBuffer(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_UpdateImageBuffer")
        fn.restype = None
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_has_focus(cls) -> Callable:
        """bool EIOS_HasFocus(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_HasFocus")
        fn.restype = ct.c_bool
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_gain_focus(cls) -> Callable:
        """void EIOS_GainFocus(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GainFocus")
        fn.restype = None
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_lose_focus(cls) -> Callable:
        """void EIOS_LoseFocus(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_LoseFocus")
        fn.restype = None
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_is_input_enabled(cls) -> Callable:
        """bool EIOS_IsInputEnabled(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_IsInputEnabled")
        fn.restype = ct.c_bool
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_set_input_enabled(cls) -> Callable:
        """void EIOS_SetInputEnabled(EIOS* eios, bool enabled) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_SetInputEnabled")
        fn.restype = None
        fn.argtypes = [EIOSPtr, ct.c_bool]
        return fn

    @property
    def _eios_get_mouse_position(cls) -> Callable:
        """void EIOS_GetMousePosition(EIOS* eios, std::int32_t* x, std::int32_t* y) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetMousePosition")
        fn.restype = None
        fn.argtypes = [EIOSPtr, IntPtr, IntPtr]
        return fn

    @property
    def _eios_get_real_mouse_position(cls) -> Callable:
        """void EIOS_GetRealMousePosition(EIOS* eios, std::int32_t* x, std::int32_t* y) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetRealMousePosition")
        fn.restype = None
        fn.argtypes = [EIOSPtr, IntPtr, IntPtr]
        return fn

    @property
    def _eios_move_mouse(cls) -> Callable:
        """void EIOS_MoveMouse(EIOS* eios, std::int32_t x, std::int32_t y) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_MoveMouse")
        fn.restype = None
        fn.argtypes = [EIOSPtr, Coordinate, Coordinate]
        return fn

    @property
    def _eios_hold_mouse(cls) -> Callable:
        """void EIOS_HoldMouse(EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_HoldMouse")
        fn.restype = None
        fn.argtypes = [EIOSPtr, Coordinate, Coordinate, ct.c_int32]
        return fn

    @property
    def _eios_release_mouse(cls) -> Callable:
        """void EIOS_ReleaseMouse(EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_ReleaseMouse")
        fn.restype = None
        fn.argtypes = [EIOSPtr, Coordinate, Coordinate, MouseButton]
        return fn

    @property
    def _eios_scroll_mouse(cls) -> Callable:
        """void EIOS_ScrollMouse(EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t lines) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_ScrollMouse")
        fn.restype = None
        fn.argtypes = [EIOSPtr, Coordinate, Coordinate, MouseButton]
        return fn

    @property
    def _eios_send_string(cls) -> Callable:
        """void EIOS_SendString(EIOS* eios, const char* string, std::int32_t keywait, std::int32_t keymodwait) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_SendString")
        fn.restype = None
        fn.argtypes = [EIOSPtr, CStr, ct.c_int32, ct.c_int32]
        return fn

    @property
    def _eios_hold_key(cls) -> Callable:
        """void EIOS_HoldKey(EIOS* eios, std::int32_t key) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_HoldKey")
        fn.restype = None
        fn.argtypes = [EIOSPtr, KeyCode]
        return fn

    @property
    def _eios_release_key(cls) -> Callable:
        """void EIOS_ReleaseKey(EIOS* eios, std::int32_t key) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_ReleaseKey")
        fn.restype = None
        fn.argtypes = [EIOSPtr, KeyCode]
        return fn

    @property
    def _eios_is_key_held(cls) -> Callable:
        """bool EIOS_IsKeyHeld(EIOS* eios, std::int32_t key) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_IsKeyHeld")
        fn.restype = ct.c_bool
        fn.argtypes = [EIOSPtr, KeyCode]
        return fn

    @property
    def _eios_get_keyboard_speed(cls) -> Callable:
        """std::int32_t EIOS_GetKeyboardSpeed(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetKeyboardSpeed")
        fn.restype = ct.c_int32
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_set_keyboard_speed(cls) -> Callable:
        """void EIOS_SetKeyboardSpeed(EIOS* eios, std::int32_t speed) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_SetKeyboardSpeed")
        fn.restype = None
        fn.argtypes = [EIOSPtr, ct.c_int32]
        return fn

    @property
    def _eios_get_keyboard_repeat_delay(cls) -> Callable:
        """std::int32_t EIOS_GetKeyboardRepeatDelay(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetKeyboardRepeatDelay")
        fn.restype = ct.c_int32
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_set_keyboard_repeat_delay(cls) -> Callable:
        """void EIOS_SetKeyboardRepeatDelay(EIOS* eios, std::int32_t delay) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_SetKeyboardRepeatDelay")
        fn.restype = None
        fn.argtypes = [EIOSPtr, ct.c_int32]
        return fn

    @property
    def _eios_pair_client(cls) -> Callable:
        """EIOS* EIOS_PairClient(pid_t pid) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_PairClient")
        fn.restype = EIOSPtr
        fn.argtypes = [PID]
        return fn

    @property
    def _eios_kill_client_pid(cls) -> Callable:
        """void EIOS_KillClientPID(pid_t pid) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_KillClientPID")
        fn.restype = None
        fn.argtypes = [PID]
        return fn

    @property
    def _eios_kill_client(cls) -> Callable:
        """void EIOS_KillClient(EIOS* eios) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_KillClient")
        fn.restype = None
        fn.argtypes = [EIOSPtr]
        return fn

    @property
    def _eios_kill_zombie_clients(cls) -> Callable:
        """void EIOS_KillZombieClients() noexcept;"""
        fn = getattr(cls.wdll, "EIOS_KillZombieClients")
        fn.restype = None
        fn.argtypes = []
        return fn

    @property
    def _eios_get_clients(cls) -> Callable:
        """std::size_t EIOS_GetClients(bool unpaired_only) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetClients")
        fn.restype = ct.c_size_t
        fn.argtypes = [ct.c_bool]
        return fn

    @property
    def _eios_get_client_pid(cls) -> Callable:
        """pid_t EIOS_GetClientPID(std::size_t index) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_GetClientPID")
        fn.restype = PID
        fn.argtypes = [ct.c_size_t]
        return fn

    @property
    def _eios_inject(cls) -> Callable:
        """void EIOS_Inject(const char* process_name) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_Inject")
        fn.restype = None
        fn.argtypes = [CStr]
        return fn

    @property
    def _eios_inject_pid(cls) -> Callable:
        """void EIOS_Inject_PID(std::int32_t pid) noexcept;"""
        fn = getattr(cls.wdll, "EIOS_Inject_PID")
        fn.restype = None
        fn.argtypes = [PID]
        return fn

    @property
    def _reflect_get_eios(cls) -> Callable:
        """EIOS* Reflect_GetEIOS(std::int32_t pid) noexcept;"""
        fn = getattr(cls.wdll, "Reflect_GetEIOS")
        fn.restype = EIOSPtr
        fn.argtypes = [PID]
        return fn

    @property
    def _reflect_is_same_object(cls) -> Callable:
        """jboolean Reflect_IsSame_Object(EIOS* eios, jobject first, jobject second) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_GetEIOS")
        fn.restype = ct.c_bool
        fn.argtypes = [EIOSPtr, JObject, JObject]
        return fn

    @property
    def _reflect_instance_of(cls) -> Callable:
        """jboolean Reflect_InstanceOf(EIOS* eios, jobject object, const char* cls) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_InstanceOf")
        fn.restype = ct.c_bool
        fn.argtypes = [EIOSPtr, JObject, CStr]
        return fn

    @property
    def _reflect_object(cls) -> Callable:
        """jobject Reflect_Object(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Object")
        fn.restype = JObject
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_release_object(cls) -> Callable:
        """void Reflect_Release_Object(EIOS* eios, jobject object) noexcept;"""
        fn = getattr(cls.wdll, "Reflect_Release_Object")
        fn.restype = None
        fn.argtypes = [EIOSPtr, JObject]
        return fn

    @property
    def _reflect_release_objects(cls) -> Callable:
        """void Reflect_Release_Object(EIOS* eios, jobject object) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Release_Objects")
        fn.restype = None
        fn.argtypes = [EIOSPtr, ct.POINTER(JArray), ct.c_size_t]
        return fn

    @property
    def _reflect_bool(cls) -> Callable:
        """bool Reflect_Bool(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Bool")
        fn.restype = ct.c_bool
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_char(cls) -> Callable:
        """char Reflect_Char(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Char")
        fn.restype = ct.c_char
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_byte(cls) -> Callable:
        """std::uint8_t Reflect_Byte(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Byte")
        fn.restype = ct.c_int8
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_short(cls) -> Callable:
        """std::int16_t Reflect_Short(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Short")
        fn.restype = ct.c_int16
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_int(cls) -> Callable:
        """std::int32_t Reflect_Int(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Int")
        fn.restype = ct.c_int32
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_long(cls) -> Callable:
        """std::int64_t Reflect_Long(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Long")
        fn.restype = ct.c_int64
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_float(cls) -> Callable:
        """float Reflect_Float(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Float")
        fn.restype = ct.c_float
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_double(cls) -> Callable:
        """double Reflect_Double(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Double")
        fn.restype = ct.c_double
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_string(cls) -> Callable:
        """void Reflect_String(EIOS* eios,jobject object,const char* cls,const char* field,const char* desc,char* output, std::size_t output_size) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_String")
        fn.restype = None
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr, ct.c_char_p, ct.c_size_t]
        return fn

    @property
    def _reflect_array(cls) -> Callable:
        """jarray Reflect_Array(EIOS* eios,jobject object,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array")
        fn.restype = JObject
        fn.argtypes = [EIOSPtr, JObject, CStr, CStr, CStr]
        return fn

    @property
    def _reflect_array_with_size(cls) -> Callable:
        """jarray Reflect_Array_With_Size(EIOS* eios,jobject object,std::size_t* output_size,const char* cls,const char* field, const char* desc) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_With_Size")
        fn.restype = JObject
        fn.argtypes = [EIOSPtr, JObject, ct.POINTER(ct.c_size_t), CStr, CStr, CStr]
        return fn

    @property
    def _reflect_array_size(cls) -> Callable:
        """std::size_t Reflect_Array_Size(EIOS* eios, jarray array) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_Size")
        fn.argtypes = [EIOSPtr, JArray]
        fn.restype = ct.c_size_t
        return fn

    @property
    def _reflect_array_index(cls) -> Callable:
        """void* Reflect_Array_Index(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t index, std::size_t length) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_Index")
        fn.restype = ct.c_void_p
        fn.argtypes = [EIOSPtr, JArray, _type, ct.c_size_t, ct.c_size_t]
        return fn

    @property
    def _reflect_array_index2d(cls) -> Callable:
        """void* Reflect_Array_Index2D(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_Index2D")
        fn.restype = ct.c_void_p
        fn.argtypes = [
            EIOSPtr,
            JArray,
            _type,
            ct.c_size_t,
            ct.c_int32,
            ct.c_int32,
        ]
        return fn

    @property
    def _reflect_array_index3d(cls) -> Callable:
        """void* Reflect_Array_Index3D(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_Index3D")
        fn.restype = ct.c_void_p
        fn.argtypes = [
            EIOSPtr,
            JArray,
            _type,
            ct.c_size_t,
            ct.c_int32,
            ct.c_int32,
            ct.c_int32,
        ]
        return fn

    @property
    def _reflect_array_index4d(cls) -> Callable:
        """void* Reflect_Array_Index4D(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z, std::int32_t w) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_Index4D")
        fn.restype = ct.c_void_p
        fn.argtypes = [
            EIOSPtr,
            JArray,
            _type,
            ct.c_size_t,
            ct.c_int32,
            ct.c_int32,
            ct.c_int32,
            ct.c_int32,
        ]
        return fn

    @property
    def _reflect_array_indices(cls) -> Callable:
        """void* Reflect_Array_Indices(EIOS* eios, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length) noexcept;"""
        fn = getattr(cls.cdll, "Reflect_Array_Indices")
        fn.restype = ct.c_void_p
        fn.argtypes = [EIOSPtr, JArray, ct.c_uint, IntPtr, ct.c_size_t]
        return fn
