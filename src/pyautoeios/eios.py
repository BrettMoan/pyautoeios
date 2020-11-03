"""
WIP: A Python wrapper for Brandons RemoteInput/Reflection for OSRS 

Resources:
    Definitions of functions from headers: 
        https://gist.github.com/Brandon-T/530ffc8780920dc12919af8d15ebac3f
    Hex code constants: 
        https://gist.github.com/kkusch/245bb80ec4e7ab4d8cdc6b7eeb3f330f#file-hex_keycodes-py
    ctypes: 
        https://docs.python.org/3/library/ctypes.html

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
            ERRORS: can't import. throws the error: 
            `AttributeError: function 'EIOS_IsMouseButtonHeld' not found`
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
from enum import Enum
import platform
from typing import Tuple, List

try:
    from importlib.resources import files

    _LIB_DIR = files(__package__) / "lib"
except ImportError:
    import pkg_resources
    import pathlib

    _LIB_DIR = pathlib.Path(pkg_resources.resource_filename(__package__, "lib"))

import psutil

from pyautoeios.hooks import THook

EIOSPtr = ctypes.c_void_p
JObject = ctypes.c_void_p
JArray = ctypes.c_void_p
ClientOffset = ctypes.c_int
PID = ctypes.c_int
KeyCode = ctypes.c_int32
Coordinate = ctypes.c_int32
MouseButton = ctypes.c_int32
IntPtr = ctypes.POINTER(ctypes.c_int32)
cstr = ctypes.c_char_p


CLIENTS = ["JagexLauncher.exe", "RuneLite.exe", "OpenOSRS.exe"]


class ReflectionArrayType(Enum):
    RI_CHAR = 0
    RI_BYTE = 1
    RI_BOOLEAN = 2
    RI_SHORT = 3
    RI_INT = 4
    RI_LONG = 5
    RI_FLOAT = 6
    RI_DOUBLE = 7
    RI_STRING = 8
    RI_OBJECT = 9


def get_client_pids() -> dict:
    return {
        process.info["pid"]
        for process in psutil.process_iter(["pid", "name"])
        if process.info["name"] in CLIENTS
    }


class EIOS:
    """Class to wrap the remoteinput methods."""

    _clients = {}
    """classvariable to hold the list of clients PIDS and their EIOS pointers"""

    _objects = {}
    """classvariable to track all object pointers, so they can be free'd"""

    # on windows we need to use _stdcall for methods from Plugin.hxx
    if platform.system() == "Windows":
        # checking the size of byte is is the most reliable method for determining
        # whether the python interpeter is 32 bit or not
        if ctypes.sizeof(ctypes.c_void_p) == 4:
            _dll_file = "libRemoteInput-i686.dll"
        else:
            _dll_file = "libRemoteInput-x86_64.dll"
        _cdecl = ctypes.CDLL(str(_LIB_DIR / _dll_file))
        _stdcall = ctypes.WinDLL(str(_LIB_DIR / _dll_file))

    # on non-windows platforms, we can always use a CDLL, so set both variables
    # to the same DLL
    elif platform.system() == "Darwin":
        _cdecl = _stdcall = ctypes.CDLL(str(_LIB_DIR / "libRemoteInput-x86_64.dylib"))

    else:
        _cdecl = _stdcall = ctypes.CDLL(str(_LIB_DIR / "libRemoteInput-x86_64.so"))

    """_cdecl & _stdcall are classvariable as libraries only need loaded once

    methods from `Plugin.hxx` uses _stdcall (windows only)
    methods from `EIOS.hxx` uses _cdecl (all platforms)
    """

    def __init__(self, pid=None):
        self._eios_ptr = None
        """pointer for the EIOS binding to the DLL"""

        self._pid = None
        """pid for the rs client"""

        # if an explict pid wasn't passed, find the first pid, that isn't
        # already bound to a client. assume any pid
        # not alreadyu in our class variable as an "unbound" pid.
        if not pid:
            pids = get_client_pids()
            for p in pids:
                if p not in self._clients.keys():
                    pid = p
                    break
            if pid is None:
                raise IOError(f"All {len(pids)} clients already bound to.")

        # if an explict pid is passed, still check for it.
        elif pid in self._clients.keys():
            raise IOError("That Client is already paired")

        self._pid = pid
        self._EIOS_Inject_PID(pid)
        self._eios_ptr = self._EIOS_PairClient(pid)
        if self._eios_ptr == 0:
            raise IOError("Couldn't find an available client.")

        self._clients[pid] = self._eios_ptr
        self._objects[pid] = {}
        """An individual dict for just this client's object pointers"""

    def __del__(self):
        """Free object pointers during garbage collection.

        We track each object we reflect when the object is created.
            Although each object *should* free itself when it leave scope
            with the RSTRype.__del__, we add an extra one here at the EIOS
            level to catch any that left hanging, such as is the case with
            circular references. in normal execution, the EIOS will always
            clear, so its the last stand against memory leaks.
        """
        if self._pid:
            print(f"unpairing client EIOS({self._pid})")
            for ref in self._objects.pop(self._pid).keys():
                print(f"freeing {ref}")
                self._Reflect_Release_Object(ref)
            self._clients.pop(self._pid)
        if self._eios_ptr:
            self._EIOS_ReleaseTarget()

    def __str__(self):
        """Simple string repreentation."""
        return f"EIOS({self._pid})"

    def __repr__(self):
        """Simple string repreentation."""
        return f"EIOS({self._pid})"

    _stdcall.EIOS_RequestTarget.restype = EIOSPtr
    _stdcall.EIOS_RequestTarget.argtypes = [cstr]

    def _EIOS_RequestTarget(self, initstr: str) -> EIOSPtr:
        """Wrap EIOS_RequestTarget.

        EIOS* EIOS_RequestTarget(
            const char* initargs
        ) noexcept;
        """
        return self._stdcall.EIOS_RequestTarget(bytes(initstr, encoding="utf8"))

    _stdcall.EIOS_ReleaseTarget.restype = None
    _stdcall.EIOS_ReleaseTarget.argtypes = [EIOSPtr]

    def _EIOS_ReleaseTarget(self) -> None:
        """Wrap EIOS_ReleaseTarget.

        void EIOS_ReleaseTarget(
            EIOS* eios
        ) noexcept;
        """
        self._stdcall.EIOS_ReleaseTarget(self._eios_ptr)

    _stdcall.EIOS_GetTargetDimensions.restype = None
    _stdcall.EIOS_GetTargetDimensions.argtypes = [EIOSPtr, IntPtr, IntPtr]

    def _EIOS_GetTargetDimensions(self) -> Tuple[int, int]:
        """Wrap EIOS_GetTargetDimensions.

        void EIOS_GetTargetDimensions(
            EIOS* eios, std::int32_t* width, std::int32_t* height
        ) noexcept;
        :return: width, height
        """
        width = ctypes.c_int32()
        height = ctypes.c_int32()
        self._stdcall.EIOS_GetTargetDimensions(
            self._eios_ptr, ctypes.byref(width), ctypes.byref(height)
        )
        return (width.value, height.value)

    _stdcall.EIOS_GetImageBuffer.restype = ctypes.POINTER(ctypes.c_uint8)
    _stdcall.EIOS_GetImageBuffer.argtypes = [EIOSPtr]

    def _EIOS_GetImageBuffer(self):
        """Wrap EIOS_GetImageBuffer.

        std::uint8_t* EIOS_GetImageBuffer(
            EIOS* eios
        ) noexcept;
        """
        buffer = self._stdcall.EIOS_GetImageBuffer(self._eios_ptr)
        return buffer

    _stdcall.EIOS_GetDebugImageBuffer.restype = ctypes.POINTER(ctypes.c_uint8)
    _stdcall.EIOS_GetDebugImageBuffer.argtypes = [EIOSPtr]

    def _EIOS_GetDebugImageBuffer(self):
        """Wrap EIOS_GetDebugImageBuffer.

        std::uint8_t* EIOS_GetDebugImageBuffer(
            EIOS* eios
        ) noexcept;
        """
        buffer = self._stdcall.EIOS_GetDebugImageBuffer(self._eios_ptr)
        return buffer

    _stdcall.EIOS_SetGraphicsDebugging.restype = None
    _stdcall.EIOS_SetGraphicsDebugging.argtypes = [EIOSPtr, ctypes.c_bool]

    def _EIOS_SetGraphicsDebugging(self, enabled: bool):
        """Wrap EIOS_SetGraphicsDebugging.

        void EIOS_SetGraphicsDebugging(
            EIOS* eios, bool enabled
        ) noexcept;
        """
        self._stdcall.EIOS_SetGraphicsDebugging(self._eios_ptr, enabled)

    _stdcall.EIOS_UpdateImageBuffer.restype = None
    _stdcall.EIOS_UpdateImageBuffer.argtypes = [EIOSPtr]

    def _EIOS_UpdateImageBuffer(self) -> None:
        """Wrap EIOS_UpdateImageBuffer.

        void EIOS_UpdateImageBuffer(
            EIOS* eios
        ) noexcept;
        """
        self._stdcall.EIOS_UpdateImageBuffer(self._eios_ptr)

    _stdcall.EIOS_HasFocus.restype = ctypes.c_bool
    _stdcall.EIOS_HasFocus.argtypes = [EIOSPtr]

    def _EIOS_HasFocus(self) -> bool:
        """Wrap EIOS_HasFocus.

        bool EIOS_HasFocus(
            EIOS* eios
        ) noexcept;
        """
        return self._stdcall.EIOS_HasFocus(self._eios_ptr)

    _stdcall.EIOS_GainFocus.restype = None
    _stdcall.EIOS_GainFocus.argtypes = [EIOSPtr]

    def _EIOS_GainFocus(self) -> None:
        """Wrap EIOS_GainFocus.

        void EIOS_GainFocus(
            EIOS* eios
        ) noexcept;
        """
        self._stdcall.EIOS_GainFocus(self._eios_ptr)

    _stdcall.EIOS_LoseFocus.restype = None
    _stdcall.EIOS_LoseFocus.argtypes = [EIOSPtr]

    def _EIOS_LoseFocus(self) -> None:
        """Wrap EIOS_LoseFocus.

        void EIOS_LoseFocus(
            EIOS* eios
        ) noexcept;
        """
        self._stdcall.EIOS_LoseFocus(self._eios_ptr)

    _stdcall.EIOS_IsInputEnabled.restype = ctypes.c_bool
    _stdcall.EIOS_IsInputEnabled.argtypes = [EIOSPtr]

    def _EIOS_IsInputEnabled(self) -> bool:
        """Wrap EIOS_IsInputEnabled.

        bool EIOS_IsInputEnabled(
            EIOS* eios
        ) noexcept;
        """
        return self._stdcall.EIOS_IsInputEnabled(self._eios_ptr)

    _stdcall.EIOS_SetInputEnabled.restype = None
    _stdcall.EIOS_SetInputEnabled.argtypes = [EIOSPtr, ctypes.c_bool]

    def _EIOS_SetInputEnabled(self, enabled: bool) -> None:
        """Wrap EIOS_SetInputEnabled.

        void EIOS_SetInputEnabled(
            EIOS* eios, bool enabled
        ) noexcept;
        """
        self._stdcall.EIOS_SetInputEnabled(self._eios_ptr, enabled)

    _stdcall.EIOS_GetMousePosition.restype = None
    _stdcall.EIOS_GetMousePosition.argtypes = [EIOSPtr, IntPtr, IntPtr]

    def _EIOS_GetMousePosition(self) -> Tuple[int, int]:
        """Wrap EIOS_GetMousePosition.

        void EIOS_GetMousePosition(
            EIOS* eios, std::int32_t* x, std::int32_t* y
        ) noexcept;
        """
        x = ctypes.c_int32()
        y = ctypes.c_int32()
        self._stdcall.EIOS_GetMousePosition(
            self._eios_ptr, ctypes.byref(x), ctypes.byref(y)
        )
        return (x.value, y.value)

    _stdcall.EIOS_GetRealMousePosition.restype = None
    _stdcall.EIOS_GetRealMousePosition.argtypes = [EIOSPtr, IntPtr, IntPtr]

    def _EIOS_GetRealMousePosition(self) -> Tuple[int, int]:
        """Wrap EIOS_GetRealMousePosition.

        void EIOS_GetRealMousePosition(
            EIOS* eios, std::int32_t* x, std::int32_t* y
        ) noexcept;
        """
        x = ctypes.c_int32()
        y = ctypes.c_int32()
        self._stdcall.EIOS_GetRealMousePosition(
            self._eios_ptr, ctypes.byref(x), ctypes.byref(y)
        )
        return (x.value, y.value)

    _stdcall.EIOS_MoveMouse.restype = None
    _stdcall.EIOS_MoveMouse.argtypes = [EIOSPtr, Coordinate, Coordinate]

    def _EIOS_MoveMouse(self, x: int, y: int) -> None:
        """Wrap EIOS_MoveMouse.

        void EIOS_MoveMouse(
            EIOS* eios, std::int32_t x, std::int32_t y
        ) noexcept;
        """
        self._stdcall.EIOS_MoveMouse(self._eios_ptr, x, y)

    _stdcall.EIOS_HoldMouse.restype = None
    _stdcall.EIOS_HoldMouse.argtypes = [EIOSPtr, Coordinate, Coordinate, ctypes.c_int32]

    def _EIOS_HoldMouse(self, x: int, y: int, button: int) -> None:
        """Wrap EIOS_HoldMouse.

        void EIOS_HoldMouse(
            EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button
        ) noexcept;
        """
        self._stdcall.EIOS_HoldMouse(self._eios_ptr, x, y, button)

    _stdcall.EIOS_ReleaseMouse.restype = None
    _stdcall.EIOS_ReleaseMouse.argtypes = [EIOSPtr, Coordinate, Coordinate, MouseButton]

    def _EIOS_ReleaseMouse(self, x: int, y: int, button: int) -> None:
        """Wrap EIOS_ReleaseMouse.

        void EIOS_ReleaseMouse(
            EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button
        ) noexcept;
        """
        self._stdcall.EIOS_ReleaseMouse(self._eios_ptr, x, y, button)

    _stdcall.EIOS_ScrollMouse.restype = None
    _stdcall.EIOS_ScrollMouse.argtypes = [EIOSPtr, Coordinate, Coordinate, MouseButton]

    def _EIOS_ScrollMouse(self, x: int, y: int, lines: int) -> None:
        """Wrap EIOS_ScrollMouse.

        void EIOS_ScrollMouse(
            EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t lines
        ) noexcept;
        """
        self._stdcall.EIOS_ScrollMouse(self._eios_ptr, x, y, lines)

    # TODO: EIOS_IsMouseButtonHeld appears to be missing form the DLL???
    # always throws a `AttributeError: function 'EIOS_IsMouseButtonHeld' not found` ERROR

    # _stdcall.EIOS_IsMouseButtonHeld.restype = ctypes.c_bool
    # _stdcall.EIOS_IsMouseButtonHeld.argtypes = [EIOSPtr, MouseButton]

    def _EIOS_IsMouseButtonHeld(self, button: int) -> bool:
        """Wrap EIOS_IsMouseButtonHeld.

        TODO:
            this appears to be missing from the DLL.
                adding the restype and argtype assignments throws a
                "function doesn't exist" error

        bool EIOS_IsMouseButtonHeld(
            EIOS* eios, std::int32_t button
        ) noexcept;
        """
        raise NotImplementedError(
            "EIOS_IsMouseButtonHeld appears to be missing form the DLL"
        )
        # return self._stdcall.EIOS_IsMouseButtonHeld(self._eios_ptr, button)

    _stdcall.EIOS_SendString.restype = None
    _stdcall.EIOS_SendString.argtypes = [EIOSPtr, cstr, ctypes.c_int32, ctypes.c_int32]

    def _EIOS_SendString(self, text: str, keywait: int, keymodwait: int) -> None:
        """Wrap EIOS_SendString.

        void EIOS_SendString(
            EIOS* eios, const char* string, std::int32_t keywait, std::int32_t keymodwait
        ) noexcept;
        """
        _text = bytes(text, encoding="utf8")
        self._stdcall.EIOS_SendString(self._eios_ptr, _text, keywait, keymodwait)

    _stdcall.EIOS_HoldKey.restype = None
    _stdcall.EIOS_HoldKey.argtypes = [EIOSPtr, KeyCode]

    def _EIOS_HoldKey(self, key: int) -> None:
        """Wrap EIOS_HoldKey.

        void EIOS_HoldKey(
            EIOS* eios, std::int32_t key
        ) noexcept;
        """
        self._stdcall.EIOS_HoldKey(self._eios_ptr, key)

    _stdcall.EIOS_ReleaseKey.restype = None
    _stdcall.EIOS_ReleaseKey.argtypes = [EIOSPtr, KeyCode]

    def _EIOS_ReleaseKey(self, key: int) -> None:
        """Wrap EIOS_ReleaseKey.

        void EIOS_ReleaseKey(
            EIOS* eios, std::int32_t key
        ) noexcept;
        """
        self._stdcall.EIOS_ReleaseKey(self._eios_ptr, key)

    _stdcall.EIOS_IsKeyHeld.restype = ctypes.c_bool
    _stdcall.EIOS_IsKeyHeld.argtypes = [EIOSPtr, KeyCode]

    def _EIOS_IsKeyHeld(self, key: int) -> bool:
        """Wrap EIOS_IsKeyHeld.

        bool EIOS_IsKeyHeld(
            EIOS* eios, std::int32_t key
        ) noexcept;
        """
        return self._stdcall.EIOS_IsKeyHeld(self._eios_ptr, key)

    _stdcall.EIOS_GetKeyboardSpeed.restype = ctypes.c_int32
    _stdcall.EIOS_GetKeyboardSpeed.argtypes = [EIOSPtr]

    def _EIOS_GetKeyboardSpeed(self) -> int:
        """Wrap EIOS_GetKeyboardSpeed.

        std::int32_t EIOS_GetKeyboardSpeed(
            EIOS* eios
        ) noexcept;
        """
        return self._stdcall.EIOS_GetKeyboardSpeed(self._eios_ptr)

    _stdcall.EIOS_SetKeyboardSpeed.restype = None
    _stdcall.EIOS_SetKeyboardSpeed.argtypes = [EIOSPtr, ctypes.c_int32]

    def _EIOS_SetKeyboardSpeed(self, speed: int) -> None:
        """Wrap EIOS_SetKeyboardSpeed.

        void EIOS_SetKeyboardSpeed(
            EIOS* eios,
            std::int32_t speed
        ) noexcept;
        """
        self._stdcall.EIOS_SetKeyboardSpeed(self._eios_ptr, speed)

    _stdcall.EIOS_GetKeyboardRepeatDelay.restype = ctypes.c_int32
    _stdcall.EIOS_GetKeyboardRepeatDelay.argtypes = [EIOSPtr]

    def _EIOS_GetKeyboardRepeatDelay(self) -> int:
        """Wrap EIOS_GetKeyboardRepeatDelay.

        std::int32_t EIOS_GetKeyboardRepeatDelay(
            EIOS* eios
        ) noexcept;
        """
        return self._stdcall.EIOS_GetKeyboardRepeatDelay(self._eios_ptr)

    _stdcall.EIOS_SetKeyboardRepeatDelay.restype = None
    _stdcall.EIOS_SetKeyboardRepeatDelay.argtypes = [EIOSPtr, ctypes.c_int32]

    def _EIOS_SetKeyboardRepeatDelay(self, delay: int) -> None:
        """Wrap EIOS_SetKeyboardRepeatDelay.

        void EIOS_SetKeyboardRepeatDelay(
            EIOS* eios,
            std::int32_t delay
        ) noexcept;
        """
        self._stdcall.EIOS_SetKeyboardRepeatDelay(self._eios_ptr, delay)

    _stdcall.EIOS_PairClient.restype = EIOSPtr
    _stdcall.EIOS_PairClient.argtypes = [PID]

    def _EIOS_PairClient(self, pid: int) -> EIOSPtr:
        """Wrap EIOS_PairClient.

        EIOS* EIOS_PairClient(
            pid_t pid
        ) noexcept;
        """
        return self._stdcall.EIOS_PairClient(pid)

    _stdcall.EIOS_KillClientPID.restype = None
    _stdcall.EIOS_KillClientPID.argtypes = [PID]

    def _EIOS_KillClientPID(self, pid: int) -> None:
        """Wrap EIOS_KillClientPID.

        void EIOS_KillClientPID(
            pid_t pid
        ) noexcept;
        """
        self._stdcall.EIOS_KillClientPID(pid)

    _stdcall.EIOS_KillClient.restype = None
    _stdcall.EIOS_KillClient.argtypes = [EIOSPtr]

    def _EIOS_KillClient(self) -> None:
        """Wrap EIOS_KillClient.

        void EIOS_KillClient(
            EIOS* eios
        ) noexcept;
        """
        self._stdcall.EIOS_KillClient(self._eios_ptr)

    _stdcall.EIOS_KillZombieClients.restype = None
    _stdcall.EIOS_KillZombieClients.argtypes = []

    def _EIOS_KillZombieClients(self) -> None:
        """Wrap EIOS_KillZombieClients.

        void EIOS_KillZombieClients() noexcept;
        """
        self._stdcall.EIOS_KillZombieClients(self._eios_ptr)

    _stdcall.EIOS_GetClients.restype = ctypes.c_size_t
    _stdcall.EIOS_GetClients.argtypes = [ctypes.c_bool]

    def _EIOS_GetClients(self, unpaired_only: bool = False) -> int:
        """Wrap EIOS_GetClients.

        std::size_t EIOS_GetClients(bool unpaired_only) noexcept;

        Args:
            unpaired_only: Whether retrict to only unparied clients or all clients

        Return:
            number of clients
        """
        return self._stdcall.EIOS_GetClients(unpaired_only)

    _stdcall.EIOS_GetClientPID.restype = PID
    _stdcall.EIOS_GetClientPID.argtypes = [ctypes.c_size_t]

    def _EIOS_GetClientPID(self, index: int) -> int:
        """Wrap EIOS_GetClientPID.

        pid_t EIOS_GetClientPID(
            std::size_t index
        ) noexcept;
        """
        return self._stdcall.EIOS_GetClientPID(index)

    _cdecl.EIOS_Inject.restype = None
    _cdecl.EIOS_Inject.argtypes = [cstr]

    def _EIOS_Inject(self, process_name: str = "JagexLauncher.exe") -> None:
        """Wrap EIOS_Inject.

        void EIOS_Inject(const
        char* process_name
        ) noexcept;
        """
        self._cdecl.EIOS_Inject(process_name.encode("utf8"))

    _cdecl.EIOS_Inject_PID.restype = None
    _cdecl.EIOS_Inject_PID.argtypes = [PID]

    def _EIOS_Inject_PID(self, pid: int) -> None:
        """Wrap EIOS_Inject_PID.

        void EIOS_Inject_PID(
            std::int32_t pid
        ) noexcept;
        """
        self._cdecl.EIOS_Inject_PID(pid)

    _cdecl.Reflect_GetEIOS.restype = EIOSPtr
    _cdecl.Reflect_GetEIOS.argtypes = [PID]

    def _Reflect_GetEIOS(self, pid: int) -> EIOSPtr:
        """Wrap Reflect_GetEIOS.

        EIOS* Reflect_GetEIOS(
            std::int32_t pid
        ) noexcept;
        """
        return self._stdcall.Reflect_GetEIOS(pid)

    _stdcall.Reflect_Object.restype = JObject
    _stdcall.Reflect_Object.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Object(self, jobject: JObject, hook: THook):
        """Wrap Reflect_Object.

        jobject Reflect_Object(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        return self._stdcall.Reflect_Object(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    def _Reflect_IsSame_Object(self, first: JObject, second: JObject):
        """Wrap Reflect_IsSame_Object.

        jboolean Reflect_IsSame_Object(
            EIOS* eios, jobject first, jobject second
        ) noexcept;
        """
        raise NotImplementedError

    def _Reflect_InstanceOf(self, jobject: JObject, cls_name: str):
        """Wrap Reflect_InstanceOf.

        jboolean Reflect_InstanceOf(
            EIOS* eios, jobject object, const char* cls
        ) noexcept;
        """
        raise NotImplementedError

    _stdcall.Reflect_Release_Object.restype = None
    _stdcall.Reflect_Release_Object.argtypes = [EIOSPtr, JObject]

    def _Reflect_Release_Object(self, jobject: JObject):
        """Wrap Reflect_Release_Object.

        void Reflect_Release_Object(
            EIOS* eios, jobject object
        ) noexcept;
        """
        self._stdcall.Reflect_Release_Object(self._eios_ptr, jobject)

    def _Reflect_Release_Objects(self, objects, amount: int):
        """Wrap Reflect_Release_Objects.

        void Reflect_Release_Objects(
            EIOS* eios,
            jobject* objects,
            std::size_t amount
        ) noexcept;
        """
        raise NotImplementedError

    _stdcall.Reflect_Bool.restype = ctypes.c_bool
    _stdcall.Reflect_Bool.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Bool(self, jobject: JObject, hook: THook) -> bool:
        """Wrap Reflect_Bool.

        bool Reflect_Bool(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        return self._stdcall.Reflect_Bool(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    _stdcall.Reflect_Char.restype = ctypes.c_char
    _stdcall.Reflect_Char.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Char(self, jobject: JObject, hook: THook) -> bytes:
        """Wrap Reflect_Char.

        char Reflect_Char(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        return self._stdcall.Reflect_Char(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    _stdcall.Reflect_Byte.restype = ctypes.c_int8
    _stdcall.Reflect_Byte.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Byte(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Byte.

        std::uint8_t Reflect_Byte(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        value = self._stdcall.Reflect_Byte(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 7) % 2 ** 8 - 2 ** 7

    _stdcall.Reflect_Short.restype = ctypes.c_int16
    _stdcall.Reflect_Short.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Short(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Short.

        std::int16_t Reflect_Short(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        value = self._stdcall.Reflect_Short(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 15) % 2 ** 16 - 2 ** 15

    _stdcall.Reflect_Int.restype = ctypes.c_int32
    _stdcall.Reflect_Int.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Int(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Int.

        std::int32_t Reflect_Int(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        value = self._stdcall.Reflect_Int(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 31) % 2 ** 32 - 2 ** 31

    _stdcall.Reflect_Long.restype = ctypes.c_int64
    _stdcall.Reflect_Long.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Long(self, jobject: JObject, hook: THook) -> int:
        """Wrap Reflect_Long.

        std::int64_t Reflect_Long(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        value = self._stdcall.Reflect_Long(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )
        return ((value * hook.multiplier) + 2 ** 63) % 2 ** 64 - 2 ** 63

    def _Reflect_Float(self, jobject: JObject, hook: THook) -> float:
        """Wrap Reflect_Float.

        float Reflect_Float(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        raise NotImplementedError

    def _Reflect_Double(self, jobject: JObject, hook: THook) -> float:
        """Wrap Reflect_Double.

        double Reflect_Double(
            EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        raise NotImplementedError

    _stdcall.Reflect_String.restype = None
    _stdcall.Reflect_String.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
        cstr,
        ctypes.c_size_t,
    ]

    def _Reflect_String(self, jobject: JObject, hook: THook, max_size=100):
        """Wrap Reflect_String.

        void Reflect_String(EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc,
            char* output,
            std::size_t output_size
        ) noexcept;
        """
        output = ctypes.create_string_buffer(max_size)
        self._stdcall.Reflect_String(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc, output, max_size
        )
        return output.value.decode("utf8")

    _stdcall.Reflect_Array.restype = JObject
    _stdcall.Reflect_Array.argtypes = [
        EIOSPtr,
        JObject,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Array(self, jobject: JObject, hook: THook):
        """Wrap Reflect_Array.

        jarray Reflect_Array(EIOS* eios,
            jobject object,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        return self._stdcall.Reflect_Array(
            self._eios_ptr, jobject, hook.cls, hook.field, hook.desc
        )

    _stdcall.Reflect_Array_With_Size.restype = JObject
    _stdcall.Reflect_Array_With_Size.argtypes = [
        EIOSPtr,
        JObject,
        IntPtr,
        cstr,
        cstr,
        cstr,
    ]

    def _Reflect_Array_With_Size(self, jobject: JObject, hook: THook):
        """Wrap Reflect_Array_With_Size.

        jarray Reflect_Array_With_Size(
            EIOS* eios,
            jobject object,
            std::size_t* output_size,
            const char* cls,
            const char* field,
            const char* desc
        ) noexcept;
        """
        size = ctypes.c_int32()
        _ref = self._stdcall.Reflect_Array_With_Size(
            self._eios_ptr, jobject, ctypes.byref(size), hook.cls, hook.field, hook.desc
        )
        return (_ref, size.value)

    _stdcall.Reflect_Array_Size.argtypes = [EIOSPtr, JArray]
    _stdcall.Reflect_Array_Size.restype = ctypes.c_size_t

    def _Reflect_Array_Size(self, jarray: JArray):
        """Wrap Reflect_Array_Size.

        std::size_t Reflect_Array_Size(
            EIOS* eios,
            jarray array
        ) noexcept;
        """
        return self._stdcall.Reflect_Array_Size(self._eios_ptr, jarray)

    _stdcall.Reflect_Array_Index.restype = ctypes.c_void_p
    _stdcall.Reflect_Array_Index.argtypes = [
        EIOSPtr,
        JArray,
        ctypes.c_uint,
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]

    def _Reflect_Array_Index(
        self,
        jarray: JArray,
        data_type: int,
        index: int,
        length: int,
    ):
        """Wrap Reflect_Array_Index.

        void* Reflect_Array_Index(
            EIOS* eios,
            jarray array,
            ReflectionArrayType type,
            std::size_t index,
            std::size_t length
        ) noexcept;
        """
        return self._stdcall.Reflect_Array_Index(
            self._eios_ptr, jarray, data_type, index, length
        )

    _stdcall.Reflect_Array_Index2D.restype = ctypes.c_void_p
    _stdcall.Reflect_Array_Index2D.argtypes = [
        EIOSPtr,
        JArray,
        ctypes.c_uint,
        ctypes.c_size_t,
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]

    def _Reflect_Array_Index2D(
        self,
        jarray: JArray,
        data_type: int,
        length: int,
        x: int,
        y: int,
    ):
        """Wrap Reflect_Array_Index2D.

        void* Reflect_Array_Index2D(
            EIOS* eios,
            jarray array,
            ReflectionArrayType type,
            std::size_t length,
            std::int32_t x,
            std::int32_t y
        ) noexcept;
        """
        return self._stdcall.Reflect_Array_Index2D(
            self._eios_ptr, jarray, data_type, length, x, y
        )

    _stdcall.Reflect_Array_Index3D.restype = ctypes.c_void_p
    _stdcall.Reflect_Array_Index3D.argtypes = [
        EIOSPtr,
        JArray,
        ctypes.c_uint,
        ctypes.c_size_t,
        ctypes.c_size_t,
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]

    def _Reflect_Array_Index3D(
        self,
        jarray: JArray,
        data_type: int,
        length: int,
        x: int,
        y: int,
        z: int,
    ):
        """Wrap Reflect_Array_Index3D.

        void* Reflect_Array_Index3D(
            EIOS* eios,
            jarray array,
            ReflectionArrayType type,
            std::size_t length,
            std::int32_t x,
            std::int32_t y,
            std::int32_t z
        ) noexcept;
        """
        return self._stdcall.Reflect_Array_Index3D(
            self._eios_ptr, jarray, data_type, length, x, y, z
        )

    _stdcall.Reflect_Array_Index4D.restype = ctypes.c_void_p
    _stdcall.Reflect_Array_Index4D.argtypes = [
        EIOSPtr,
        JArray,
        ctypes.c_uint,
        ctypes.c_size_t,
        ctypes.c_size_t,
        ctypes.c_size_t,
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]

    def _Reflect_Array_Index4D(
        self,
        jarray: JArray,
        data_type: int,
        length: int,
        x: int,
        y: int,
        z: int,
        w: int,
    ):
        """Wrap Reflect_Array_Index4D.

        void* Reflect_Array_Index4D(
            EIOS* eios,
            jarray array,
            ReflectionArrayType type,
            std::size_t length,
            std::int32_t x,
            std::int32_t y,
            std::int32_t z,
            std::int32_t w
        ) noexcept;
        """
        return self._stdcall.Reflect_Array_Index4D(
            self._eios_ptr, jarray, data_type, length, x, y, z, w
        )

    _stdcall.Reflect_Array_Indices.restype = ctypes.c_void_p
    _stdcall.Reflect_Array_Indices.argtypes = [
        EIOSPtr,
        JArray,
        ctypes.c_uint,
        IntPtr,
        ctypes.c_size_t,
    ]

    def _Reflect_Array_Indices(
        self,
        jarray: JArray,
        data_type: int,
        indices: List[int],
    ):
        """Wrap Reflect_Array_Indices.

        void* Reflect_Array_Indices(
            EIOS* eios, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length
        ) noexcept;
        """
        c_array_type = ctypes.c_int * len(indices)
        c_array = c_array_type(*indices)
        return self._stdcall.Reflect_Array_Indices(
            self._eios_ptr, jarray, data_type, c_array, len(indices)
        )

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
