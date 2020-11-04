from pyautoeios import hooks
from pyautoeios.rs_node import RSNode
from pyautoeios.rs_structures import RSType


class RSNodeDeque(RSType):
    def head(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.NODEDEQUE_HEAD)
        return RSNode(self.eios, _ref)

    def current(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.NODEDEQUE_CURRENT)
        return RSNode(self.eios, _ref)
