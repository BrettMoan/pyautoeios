from pyautoeios.rs_structures import RSType
from pyautoeios import hooks


class RSNode(RSType):
    def uid(self) -> int:
        return self.eios._Reflect_Long(self.ref, hooks.NODE_UID)

    def previous(self):
        _ref = self.eios._Reflect_Object(self.ref, hooks.NODE_PREV)
        return RSNode(self.eios, _ref)

    def next(self):
        _ref = self.eios._Reflect_Object(self.ref, hooks.NODE_NEXT)
        return RSNode(self.eios, _ref)
