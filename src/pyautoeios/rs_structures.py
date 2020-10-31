import ctypes
from pyautoeios.eios import EIOS

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


class RSType:
    def __init__(self, eios: EIOS = None, ref=None):
        self.eios = eios
        self.ref = ref
        eios._objects[eios._pid][ref] = eios._objects[eios._pid].get(ref, 0) + 1
        # print(f"refcount of {self.__class__.__name__}({ref}) = {eios._objects[eios._pid][ref]}")

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.ref}) paired with EIOS({self.eios._pid})"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.ref}) paired with EIOS({self.eios._pid})"
        )

    def __del__(self):
        ref_count = self.eios._objects[self.eios._pid][self.ref]
        if ref_count == 1:
            self.eios._objects[self.eios._pid].pop(self.ref)
            self.eios._Reflect_Release_Object(self.ref)
            # print(f"refcount of {self.__class__.__name__}({self.ref}) = {ref_count-1}")
        else:
            self.eios._objects[self.eios._pid][self.ref] -= 1
            # print(f"refcount of {self.__class__.__name__}({self.ref}) = {ref_count-1}")


class RSArray(RSType):
    def __init__(self, eios: EIOS = None, ref=None, ra_type: int = None, ctype=None):
        self.ra_type = ra_type
        self.ctype = ctype
        super().__init__(eios, ref)

    def __getitem__(self, key: int = None):
        element = self.eios._Reflect_Array_Index(self.ref, self.ra_type, key, 1)
        pi = ctypes.cast(element, ctypes.POINTER(self.ctype))
        # print(f"{element = } , {pi = }, {pi.contents = }")
        return pi.contents.value


class RSIntArray(RSArray):
    def __init__(self, eios: EIOS = None, ref=None):
        super().__init__(eios, ref, RI_INT, ctypes.c_int)
