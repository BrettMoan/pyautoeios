from pyautoeios.rs_structures import RSType
from pyautoeios import hooks
from pyautoeios.rs_node import RSNode


class RSQueue(RSType):
    def head(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.QUEUE_HEAD)
        return RSNode(self.eios, _ref)
