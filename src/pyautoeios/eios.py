"""
WIP: A Python wrapper for Brandons RemoteInput/Reflection for OSRS 

Resources:
    Definitions of functions from headers: https://gist.github.com/Brandon-T/530ffc8780920dc12919af8d15ebac3f
    Hex code constants: https://gist.github.com/kkusch/245bb80ec4e7ab4d8cdc6b7eeb3f330f#file-hex_keycodes-py
    ctypes: https://docs.python.org/3/library/ctypes.html

Working: (tested with vanilla client)
    [x] EIOS_GainFocus
    [x] EIOS_GetClientPID
    [x] EIOS_GetClients
    [x] EIOS_GetMousePosition
    [x] EIOS_GetRealMousePosition
    [x] EIOS_GetTargetDimensions
    [x] EIOS_HasFocus
    [x] EIOS_HoldKey
    [x] EIOS_HoldMouse
    [x] EIOS_Inject
    [x] EIOS_LoseFocus
    [x] EIOS_MoveMouse
    [x] EIOS_PairClient
    [x] EIOS_ReleaseKey
    [x] EIOS_ReleaseMouse
    [x] EIOS_ReleaseTarget
    [x] EIOS_SendString

TODO:

    [ ] Functions that still need tested:
        [x] EIOS_GetImageBuffer 
        [ ] EIOS_GetDebugImageBuffer 
        [ ] EIOS_SetGraphicsDebugging 
        [ ] EIOS_UpdateImageBuffer 
        [ ] EIOS_ScrollMouse 
        [x] EIOS_IsMouseButtonHeld 
            ERRORS: can't import throws: `AttributeError: function 'EIOS_IsMouseButtonHeld' not found`
        [ ] EIOS_IsKeyHeld
        [ ] EIOS_GetKeyboardSpeed
        [ ] EIOS_SetKeyboardSpeed
        [ ] EIOS_GetKeyboardRepeatDelay
        [ ] EIOS_SetKeyboardRepeatDelay
        [ ] EIOS_KillClientPID
        [ ] EIOS_KillClient
        [ ] EIOS_KillZombieClients
        [ ] Reflect_GetEIOS
    
    [ ] Functions that still need written:
        [x] Reflect_Object
        [ ] Reflect_IsSame_Object
        [ ] Reflect_InstanceOf
        [x] Reflect_Release_Object
        [ ] Reflect_Release_Objects
        [x] Reflect_Bool
        [x] Reflect_Char
        [x] Reflect_Byte
        [x] Reflect_Short
        [x] Reflect_Int
        [x] Reflect_Long
        [ ] Reflect_Float
        [ ] Reflect_Double
        [x] Reflect_String
        [ ] Reflect_Array
        [ ] Reflect_Array_With_Size
        [ ] Reflect_Array_Size
        [ ] Reflect_Array_Index
        [ ] Reflect_Array_Index2D
        [ ] Reflect_Array_Index3D
        [ ] Reflect_Array_Index4D
        [ ] Reflect_Array_Indices
"""

import ctypes
import platform
from typing import Tuple

import psutil

try:
    from importlib.resources import files
    _LIB_DIR = files(__package__) / 'lib'
except ImportError:
    import pkg_resources
    import pathlib
    _LIB_DIR = pathlib.Path(pkg_resources.resource_filename(__package__, 'lib'))

from pyautoeios.hooks import THook

EIOSPtr = ctypes.c_void_p
JObject = ctypes.c_void_p
ClientOffset = ctypes.c_int
PID = ctypes.c_int
KeyCode = ctypes.c_int32
Coordinate = ctypes.c_int32
MouseButton = ctypes.c_int32
IntPtr = ctypes.POINTER(ctypes.c_int32)

CLIENTS = ["JagexLauncher.exe", "RuneLite.exe", "OpenOSRS.exe"]

def get_client_pids() -> dict:
    return {
        process.info["pid"]
        for process in psutil.process_iter(["pid", "name"])
        if process.info["name"] in CLIENTS
    }


class EIOS:
    """Class to wrap the remoteinput methods."""

    _clients = {}
    _objects = {}
    """classvariable to hold the list of clients PIDS and their EIOS pointers"""

    if platform.system() == "Windows":
        if ctypes.sizeof(ctypes.c_void_p) == 4:
            _dll_file = "libRemoteInput-i686.dll"
        else:
            _dll_file = "libRemoteInput-x86_64.dll"
        _cdecl = ctypes.CDLL(str(_LIB_DIR / _dll_file))
        _stdcall = ctypes.WinDLL(str(_LIB_DIR / _dll_file))

    elif platform.system() == "Darwin":
        _cdecl = _stdcall = ctypes.CDLL(str(_LIB_DIR / "libRemoteInput-x86_64.dylib"))

    else:
        _cdecl = _stdcall = ctypes.CDLL(str(_LIB_DIR / "libRemoteInput-x86_64.so"))
    """classvariable as libraries only need loaded once

    `EIOS.hxx` uses _cdecl
    `Plugin.hxx` uses _stdcall
    """

    def __init__(self, pid=None):
        self._eios_ptr = None
        self._pid = None
        if not pid:
            pids = get_client_pids()
            for p in pids:
                if p not in self._clients.keys():
                    pid = p
                    break
            if pid is None:
                raise IOError(f"All {len(pids)} clients already bound to.")

        elif pid in self._clients.keys():
            raise IOError("That Client is already paired")

        self._pid = pid
        self._EIOS_Inject_PID(pid)
        self._eios_ptr = self._EIOS_PairClient(pid)
        if self._eios_ptr == 0:
            raise IOError("Couldn't find an available client.")

        self._clients[pid] = self._eios_ptr
        self._objects[pid] = {}

    def __del__(self):
        if self._pid:
            print(f"unpairing client EIOS({self._pid})")
            for ref in self._objects.pop(self._pid).keys():
                print(f"freeing {ref}")
                self._Reflect_Release_Object(ref)
            self._clients.pop(self._pid)
        if self._eios_ptr:
            self._EIOS_ReleaseTarget()

    def __str__(self):
        return f"EIOS({self._pid})"

    def __repr__(self):
        return f"EIOS({self._pid})"


    _stdcall.EIOS_RequestTarget.argtypes = [ctypes.c_char_p]
    _stdcall.EIOS_RequestTarget.restype = EIOSPtr

    def _EIOS_RequestTarget(self, initstr: str) -> EIOSPtr:
        """
        EIOS* EIOS_RequestTarget(const char* initargs) noexcept;
        """
        return self._stdcall.EIOS_RequestTarget(bytes(initstr, encoding="utf8"))

    _stdcall.EIOS_ReleaseTarget.argtypes = [EIOSPtr]
    _stdcall.EIOS_ReleaseTarget.restype = None

    def _EIOS_ReleaseTarget(self) -> None:
        """
        void EIOS_ReleaseTarget(EIOS* eios) noexcept;
        """
        self._stdcall.EIOS_ReleaseTarget(self._eios_ptr)

    _stdcall.EIOS_GetTargetDimensions.argtypes = [EIOSPtr, IntPtr, IntPtr]
    _stdcall.EIOS_GetTargetDimensions.restype = None

    def _EIOS_GetTargetDimensions(self):
        """
        void EIOS_GetTargetDimensions(EIOS* eios, std::int32_t* width, std::int32_t* height) noexcept;
        :return: width, height
        """
        width = ctypes.c_int32()
        height = ctypes.c_int32()
        self._stdcall.EIOS_GetTargetDimensions(
            self._eios_ptr, ctypes.byref(width), ctypes.byref(height)
        )
        return [width.value, height.value]

    _stdcall.EIOS_GetImageBuffer.argtypes = [EIOSPtr]
    _stdcall.EIOS_GetImageBuffer.restype = ctypes.POINTER(ctypes.c_uint8)

    def _EIOS_GetImageBuffer(self):
        """
        std::uint8_t* EIOS_GetImageBuffer(EIOS* eios) noexcept;
        """
        buffer = self._stdcall.EIOS_GetImageBuffer(self._eios_ptr)
        return buffer

    _stdcall.EIOS_GetDebugImageBuffer.argtypes = [EIOSPtr]
    _stdcall.EIOS_GetDebugImageBuffer.restype = ctypes.POINTER(ctypes.c_uint8)

    def _EIOS_GetDebugImageBuffer(self):
        """
        std::uint8_t* EIOS_GetDebugImageBuffer(EIOS* eios) noexcept;
        """
        buffer = self._stdcall.EIOS_GetDebugImageBuffer(self._eios_ptr)
        return buffer

    _stdcall.EIOS_SetGraphicsDebugging.argtypes = [EIOSPtr, ctypes.c_bool]
    _stdcall.EIOS_SetGraphicsDebugging.restype = None

    def _EIOS_SetGraphicsDebugging(self, enabled: bool):
        """
        void EIOS_SetGraphicsDebugging(EIOS* eios, bool enabled) noexcept;
        """
        self._stdcall.EIOS_SetGraphicsDebugging(self._eios_ptr, enabled)

    _stdcall.EIOS_UpdateImageBuffer.argtypes = [EIOSPtr]
    _stdcall.EIOS_UpdateImageBuffer.restype = None

    def _EIOS_UpdateImageBuffer(self) -> None:
        """
        void EIOS_UpdateImageBuffer(EIOS* eios) noexcept;
        """
        self._stdcall.EIOS_UpdateImageBuffer(self._eios_ptr)

    _stdcall.EIOS_HasFocus.argtypes = [EIOSPtr]
    _stdcall.EIOS_HasFocus.restype = ctypes.c_bool

    def _EIOS_HasFocus(self) -> bool:
        """
        bool EIOS_HasFocus(EIOS* eios) noexcept;
        """
        return self._stdcall.EIOS_HasFocus(self._eios_ptr)

    _stdcall.EIOS_GainFocus.argtypes = [EIOSPtr]
    _stdcall.EIOS_GainFocus.restype = None

    def _EIOS_GainFocus(self) -> None:
        """
        void EIOS_GainFocus(EIOS* eios) noexcept;
        """
        self._stdcall.EIOS_GainFocus(self._eios_ptr)

    _stdcall.EIOS_LoseFocus.argtypes = [EIOSPtr]
    _stdcall.EIOS_LoseFocus.restype = None

    def _EIOS_LoseFocus(self) -> None:
        """
        void EIOS_LoseFocus(EIOS* eios) noexcept;
        """
        self._stdcall.EIOS_LoseFocus(self._eios_ptr)

    _stdcall.EIOS_IsInputEnabled.argtypes = [EIOSPtr]
    _stdcall.EIOS_IsInputEnabled.restype = ctypes.c_bool

    def _EIOS_IsInputEnabled(self) -> bool:
        """
        bool EIOS_IsInputEnabled(EIOS* eios) noexcept;
        """
        return self._stdcall.EIOS_IsInputEnabled(self._eios_ptr)

    _stdcall.EIOS_SetInputEnabled.argtypes = [EIOSPtr, ctypes.c_bool]
    _stdcall.EIOS_SetInputEnabled.restype = None

    def _EIOS_SetInputEnabled(self, enabled: bool) -> None:
        """
        void EIOS_SetInputEnabled(EIOS* eios, bool enabled) noexcept;
        """
        self._stdcall.EIOS_SetInputEnabled(self._eios_ptr, enabled)

    _stdcall.EIOS_GetMousePosition.argtypes = [EIOSPtr, IntPtr, IntPtr]
    _stdcall.EIOS_GetMousePosition.restype = None

    def _EIOS_GetMousePosition(self) -> Tuple[int, int]:
        """
        void EIOS_GetMousePosition(EIOS* eios, std::int32_t* x, std::int32_t* y) noexcept;
        """
        x = ctypes.c_int32()
        y = ctypes.c_int32()
        self._stdcall.EIOS_GetMousePosition(self._eios_ptr, ctypes.byref(x), ctypes.byref(y))
        return (x.value, y.value)

    _stdcall.EIOS_GetRealMousePosition.argtypes = [EIOSPtr, IntPtr, IntPtr]
    _stdcall.EIOS_GetRealMousePosition.restype = None

    def _EIOS_GetRealMousePosition(self) -> Tuple[int, int]:
        """
        void EIOS_GetRealMousePosition(EIOS* eios, std::int32_t* x, std::int32_t* y) noexcept;
        """
        x = ctypes.c_int32()
        y = ctypes.c_int32()
        self._stdcall.EIOS_GetRealMousePosition(self._eios_ptr, ctypes.byref(x), ctypes.byref(y))
        return (x.value, y.value)

    _stdcall.EIOS_MoveMouse.argtypes = [EIOSPtr, Coordinate, Coordinate]
    _stdcall.EIOS_MoveMouse.restype = None

    def _EIOS_MoveMouse(self, x: int, y: int) -> None:
        """
        void EIOS_MoveMouse(EIOS* eios, std::int32_t x, std::int32_t y) noexcept;
        """
        self._stdcall.EIOS_MoveMouse(self._eios_ptr, x, y)

    _stdcall.EIOS_HoldMouse.argtypes = [EIOSPtr, Coordinate, Coordinate, ctypes.c_int32]
    _stdcall.EIOS_HoldMouse.restype = None

    def _EIOS_HoldMouse(self, x: int, y: int, button: int) -> None:
        """
        void EIOS_HoldMouse(EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button) noexcept;
        """
        self._stdcall.EIOS_HoldMouse(self._eios_ptr, x, y, button)

    _stdcall.EIOS_ReleaseMouse.argtypes = [EIOSPtr, Coordinate, Coordinate, MouseButton]
    _stdcall.EIOS_ReleaseMouse.restype = None

    def _EIOS_ReleaseMouse(self, x: int, y: int, button: int) -> None:
        """
        void EIOS_ReleaseMouse(EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button) noexcept;
        """
        self._stdcall.EIOS_ReleaseMouse(self._eios_ptr, x, y, button)

    _stdcall.EIOS_ScrollMouse.argtypes = [EIOSPtr, Coordinate, Coordinate, MouseButton]
    _stdcall.EIOS_ScrollMouse.restype = None

    def _EIOS_ScrollMouse(self, x: int, y: int, lines: int) -> None:
        """
        void EIOS_ScrollMouse(EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t lines) noexcept;
        """
        self._stdcall.EIOS_ScrollMouse(self._eios_ptr, x, y, lines)

    # TODO: EIOS_IsMouseButtonHeld appears to be missing form the DLL???
    # always throws a `AttributeError: function 'EIOS_IsMouseButtonHeld' not found` ERROR

    # _stdcall.EIOS_IsMouseButtonHeld.argtypes = [EIOSPtr, MouseButton]
    # _stdcall.EIOS_IsMouseButtonHeld.restype = ctypes.c_bool

    # def _EIOS_IsMouseButtonHeld(self, button: int) -> bool:
    #     """
    #     bool EIOS_IsMouseButtonHeld(EIOS* eios, std::int32_t button) noexcept;
    #     """
    #     return self._stdcall.EIOS_IsMouseButtonHeld(self._eios_ptr, button)

    _stdcall.EIOS_SendString.argtypes = [EIOSPtr, ctypes.c_char_p, ctypes.c_int32, ctypes.c_int32]
    _stdcall.EIOS_SendString.restype = None

    def _EIOS_SendString(self, text: str, keywait: int, keymodwait: int) -> None:
        """
        void EIOS_SendString(EIOS* eios, const char* string, std::int32_t keywait, std::int32_t keymodwait) noexcept;
        """
        _text = bytes(text, encoding="utf8")
        self._stdcall.EIOS_SendString(self._eios_ptr, _text, keywait, keymodwait)

    _stdcall.EIOS_HoldKey.argtypes = [EIOSPtr, KeyCode]
    _stdcall.EIOS_HoldKey.restype = None

    def _EIOS_HoldKey(self, key: int) -> None:
        """
        void EIOS_HoldKey(EIOS* eios, std::int32_t key) noexcept;
        """
        self._stdcall.EIOS_HoldKey(self._eios_ptr, key)

    _stdcall.EIOS_ReleaseKey.argtypes = [EIOSPtr, KeyCode]
    _stdcall.EIOS_ReleaseKey.restype = None

    def _EIOS_ReleaseKey(self, key: int) -> None:
        """
        void EIOS_ReleaseKey(EIOS* eios, std::int32_t key) noexcept;
        """
        self._stdcall.EIOS_ReleaseKey(self._eios_ptr, key)

    _stdcall.EIOS_IsKeyHeld.argtypes = [EIOSPtr, KeyCode]
    _stdcall.EIOS_IsKeyHeld.restype = ctypes.c_bool

    def _EIOS_IsKeyHeld(self, key: int) -> bool:
        """
        bool EIOS_IsKeyHeld(EIOS* eios, std::int32_t key) noexcept;
        """
        return self._stdcall.EIOS_IsKeyHeld(self._eios_ptr, key)

    _stdcall.EIOS_GetKeyboardSpeed.argtypes = [EIOSPtr]
    _stdcall.EIOS_GetKeyboardSpeed.restype = ctypes.c_int32

    def _EIOS_GetKeyboardSpeed(self) -> int:
        """
        std::int32_t EIOS_GetKeyboardSpeed(EIOS* eios) noexcept;
        """
        return self._stdcall.EIOS_GetKeyboardSpeed(self._eios_ptr)

    _stdcall.EIOS_SetKeyboardSpeed.argtypes = [EIOSPtr, ctypes.c_int32]
    _stdcall.EIOS_SetKeyboardSpeed.restype = None

    def _EIOS_SetKeyboardSpeed(self, speed: int) -> None:
        """
        void EIOS_SetKeyboardSpeed(EIOS* eios, std::int32_t speed) noexcept;
        """
        self._stdcall.EIOS_SetKeyboardSpeed(self._eios_ptr, speed)

    _stdcall.EIOS_GetKeyboardRepeatDelay.argtypes = [EIOSPtr]
    _stdcall.EIOS_GetKeyboardRepeatDelay.restype = ctypes.c_int32

    def _EIOS_GetKeyboardRepeatDelay(self) -> int:
        """
        std::int32_t EIOS_GetKeyboardRepeatDelay(EIOS* eios) noexcept;
        """
        return self._stdcall.EIOS_GetKeyboardRepeatDelay(self._eios_ptr)

    _stdcall.EIOS_SetKeyboardRepeatDelay.argtypes = [EIOSPtr, ctypes.c_int32]
    _stdcall.EIOS_SetKeyboardRepeatDelay.restype = None

    def _EIOS_SetKeyboardRepeatDelay(self, delay: int) -> None:
        """
        void EIOS_SetKeyboardRepeatDelay(EIOS* eios, std::int32_t delay) noexcept;
        """
        self._stdcall.EIOS_SetKeyboardRepeatDelay(self._eios_ptr, delay)

    _stdcall.EIOS_PairClient.argtypes = [PID]
    _stdcall.EIOS_PairClient.restype = EIOSPtr

    def _EIOS_PairClient(self, pid: int) -> EIOSPtr:
        """
        EIOS* EIOS_PairClient(pid_t pid) noexcept;
        """
        return self._stdcall.EIOS_PairClient(pid)

    _stdcall.EIOS_KillClientPID.argtypes = [PID]
    _stdcall.EIOS_KillClientPID.restype = None

    def _EIOS_KillClientPID(self, pid: int) -> None:
        """
        void EIOS_KillClientPID(pid_t pid) noexcept;
        """
        self._stdcall.EIOS_KillClientPID(pid)

    _stdcall.EIOS_KillClient.argtypes = [EIOSPtr]
    _stdcall.EIOS_KillClient.restype = None

    def _EIOS_KillClient(self) -> None:
        """
        void EIOS_KillClient(EIOS* eios) noexcept;
        """
        self._stdcall.EIOS_KillClient(self._eios_ptr)


    _stdcall.EIOS_KillZombieClients.argtypes = []
    _stdcall.EIOS_KillZombieClients.restype = None

    def _EIOS_KillZombieClients(self) -> None:
        """
        void EIOS_KillZombieClients() noexcept;
        """
        self._stdcall.EIOS_KillZombieClients(self._eios_ptr)

    _stdcall.EIOS_GetClients.argtypes = [ctypes.c_bool]
    _stdcall.EIOS_GetClients.restype = ctypes.c_size_t 

    def _EIOS_GetClients(self, unpaired_only: bool = False) -> int:
        """
        std::size_t EIOS_GetClients(bool unpaired_only) noexcept;

        :param unpaired_only: Should return only unparied clients or all clients
        :type unpaired_only: bool

        :return: injectedtargets
        :rtype: Int
        """
        return self._stdcall.EIOS_GetClients(unpaired_only)

    _stdcall.EIOS_GetClientPID.argtypes = [ctypes.c_size_t]
    _stdcall.EIOS_GetClientPID.restype = PID

    def _EIOS_GetClientPID(self, index: int) -> int:
        """
        pid_t EIOS_GetClientPID(std::size_t index) noexcept;
        """
        return self._stdcall.EIOS_GetClientPID(index)

    _cdecl.EIOS_Inject.argtypes = [ctypes.c_char_p]
    _cdecl.EIOS_Inject.restype = None

    def _EIOS_Inject(self, process_name: str = "JagexLauncher.exe") -> None:
        """
        void EIOS_Inject(const char* process_name) noexcept;
        """
        self._cdecl.EIOS_Inject(process_name.encode("utf8"))

    _cdecl.EIOS_Inject_PID.argtypes = [PID]
    _cdecl.EIOS_Inject_PID.restype = None

    def _EIOS_Inject_PID(self, pid: int) -> None:
        """
        void EIOS_Inject_PID(std::int32_t pid) noexcept;
        """
        self._cdecl.EIOS_Inject_PID(pid)

    _cdecl.Reflect_GetEIOS.argtypes = [PID]
    _cdecl.Reflect_GetEIOS.restype = EIOSPtr

    def _Reflect_GetEIOS(self, pid: int) -> EIOSPtr:
        """
        EIOS* Reflect_GetEIOS(std::int32_t pid) noexcept;
        """
        return self._stdcall.Reflect_GetEIOS(pid)


    _stdcall.Reflect_Object.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Object.restype = JObject


    def _Reflect_Object(self, jobject:JObject, hook:THook):
        """
        jobject Reflect_Object(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        return self._stdcall.Reflect_Object(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8"))

    # def _Reflect_IsSame_Object(self, jobject first, jobject second):
    #     """
    #     jboolean Reflect_IsSame_Object(EIOS* eios, jobject first, jobject second) noexcept;
    #     """
    #     pass

    # def _Reflect_InstanceOf(self, jobject:JObject, const char* cls):
    #     """
    #     jboolean Reflect_InstanceOf(EIOS* eios, jobject object, const char* cls) noexcept;
    #     """
    #     pass

    _stdcall.Reflect_Release_Object.argtypes = [EIOSPtr, JObject]
    _stdcall.Reflect_Release_Object.restype = None

    def _Reflect_Release_Object(self, jobject:JObject):
        """
        void Reflect_Release_Object(EIOS* eios, jobject object) noexcept;
        """
        self._stdcall.Reflect_Release_Object(self._eios_ptr, jobject)

    # def _Reflect_Release_Objects(self, jobject* objects, std::size_t amount):
    #     """
    #     void Reflect_Release_Objects(EIOS* eios, jobject* objects, std::size_t amount) noexcept;
    #     """
    #     pass

    _stdcall.Reflect_Bool.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Bool.restype = ctypes.c_bool

    def _Reflect_Bool(self, jobject:JObject, hook:THook) -> bool:
        """
        bool Reflect_Bool(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        return self._stdcall.Reflect_Bool(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8"))

    _stdcall.Reflect_Char.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Char.restype = ctypes.c_char

    def _Reflect_Char(self, jobject:JObject, hook:THook) -> bytes:
        """
        char Reflect_Char(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        return self._stdcall.Reflect_Char(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8"))

    _stdcall.Reflect_Byte.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Byte.restype = ctypes.c_int8

    def _Reflect_Byte(self, jobject:JObject, hook:THook) -> int:
        """
        std::uint8_t Reflect_Byte(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        value = self._stdcall.Reflect_Byte(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8")) * hook.multiplier
        return (value + 2**7) % 2**8 - 2**7

    _stdcall.Reflect_Short.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Short.restype = ctypes.c_int16

    def _Reflect_Short(self, jobject:JObject, hook:THook) -> int:
        """
        std::int16_t Reflect_Short(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        value = self._stdcall.Reflect_Short(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8")) * hook.multiplier
        return (value + 2**15) % 2**16 - 2**15


    _stdcall.Reflect_Int.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Int.restype = ctypes.c_int32

    def _Reflect_Int(self, jobject:JObject, hook:THook) -> int:
        """
        std::int32_t Reflect_Int(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        value = self._stdcall.Reflect_Int(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8")) * hook.multiplier
        return (value + 2**31) % 2**32 - 2**31

    _stdcall.Reflect_Long.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
    _stdcall.Reflect_Long.restype = ctypes.c_int64

    def _Reflect_Long(self, jobject:JObject, hook:THook) -> int:
        """
        std::int64_t Reflect_Long(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
        """
        value = self._stdcall.Reflect_Long(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8")) * hook.multiplier
        return (value + 2**63) % 2**64 - 2**63

    # def _Reflect_Float(self, jobject:JObject, hook:THook) -> float:
    #     """
    #     float Reflect_Float(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
    #     """
    #     pass

    # def _Reflect_Double(self, jobject:JObject, hook:THook) -> float:
    #     """
    #     double Reflect_Double(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
    #     """
    #     pass

    _stdcall.Reflect_String.argtypes = [EIOSPtr, JObject, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
    _stdcall.Reflect_String.restype = None

    def _Reflect_String(self, jobject:JObject, hook:THook, max_size=100):
        """
        void Reflect_String(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc, char* output, std::size_t output_size) noexcept;
        """
        output = ctypes.create_string_buffer(max_size)
        self._stdcall.Reflect_String(self._eios_ptr, jobject, hook.cls.encode("utf8"), hook.field.encode("utf8"), hook.desc.encode("utf8"), output, max_size)
        return output.value

    # def _Reflect_Array(self, jobject:JObject, hook:THook):
    #     """
    #     jarray Reflect_Array(EIOS* eios, jobject object, const char* cls, const char* field, const char* desc) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_With_Size(self, jobject:JObject, std::size_t* output_size, hook:THook):
    #     """
    #     jarray Reflect_Array_With_Size(EIOS* eios, jobject object, std::size_t* output_size, const char* cls, const char* field, const char* desc) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_Size(self, jarray array):
    #     """
    #     std::size_t Reflect_Array_Size(EIOS* eios, jarray array) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_Index(self, jarray array, ReflectionArrayType type, std::size_t index, std::size_t length):
    #     """
    #     void* Reflect_Array_Index(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t index, std::size_t length) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_Index2D(self, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y):
    #     """
    #     void* Reflect_Array_Index2D(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_Index3D(self, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z):
    #     """
    #     void* Reflect_Array_Index3D(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_Index4D(self, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z, std::int32_t w):
    #     """
    #     void* Reflect_Array_Index4D(EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z, std::int32_t w) noexcept;
    #     """
    #     pass

    # def _Reflect_Array_Indices(self, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length):
    #     """
    #     void* Reflect_Array_Indices(EIOS* eios, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length) noexcept;
    #     """
    #     pass

    ## PUBLIC FUNCTIONS, to match pythonic naming convention.
    request_target = _EIOS_RequestTarget
    release_target = _EIOS_ReleaseTarget
    get_target_dimensions = _EIOS_GetTargetDimensions
    get_image_buffer = _EIOS_GetImageBuffer
    get_debug_image_buffer = _EIOS_GetDebugImageBuffer
    set_graphics_debugging = _EIOS_SetGraphicsDebugging
    update_image_buffer = _EIOS_UpdateImageBuffer
    has_focus = _EIOS_HasFocus
    gain_focus = _EIOS_GainFocus
    lose_focus = _EIOS_LoseFocus
    is_input_enabled = _EIOS_IsInputEnabled
    set_input_enabled = _EIOS_SetInputEnabled
    get_mouse_position = _EIOS_GetMousePosition
    get_real_mouse_position = _EIOS_GetRealMousePosition
    move_mouse = _EIOS_MoveMouse
    hold_mouse = _EIOS_HoldMouse
    release_mouse = _EIOS_ReleaseMouse
    scroll_mouse = _EIOS_ScrollMouse
    send_string = _EIOS_SendString
    hold_key = _EIOS_HoldKey
    release_key = _EIOS_ReleaseKey
    is_key_held = _EIOS_IsKeyHeld
    get_keyboard_speed = _EIOS_GetKeyboardSpeed
    set_keyboard_speed = _EIOS_SetKeyboardSpeed
    get_keyboard_repeat_delay = _EIOS_GetKeyboardRepeatDelay
    set_keyboard_repeat_delay = _EIOS_SetKeyboardRepeatDelay
