from ctypes import c_void_p
from pyautoeios.eios import EIOS


class RSType:
    def __init__(self, eios:EIOS=None, ref=None):
        self.eios = eios
        self.ref = ref
        eios._objects[eios._pid][ref] = eios._objects[eios._pid].get(ref,0) + 1
        print(f"refcount of {self.__class__.__name__}({ref}) = {eios._objects[eios._pid][ref]}")

    def __str__(self):
        return f"{self.__class__.__name__}({self.ref}) paired with EIOS({self.eios._pid})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ref}) paired with EIOS({self.eios._pid})"


    def __del__(self):
        ref_count = self.eios._objects[self.eios._pid][self.ref]
        if ref_count == 1:
            self.eios._objects[self.eios._pid].pop(self.ref)
            self.eios._Reflect_Release_Object(self.ref)
            print(f"refcount of {self.__class__.__name__}({self.ref}) = {ref_count-1}")
        else:
            self.eios._objects[self.eios._pid][self.ref] -= 1
            print(f"refcount of {self.__class__.__name__}({self.ref}) = {ref_count-1}")
