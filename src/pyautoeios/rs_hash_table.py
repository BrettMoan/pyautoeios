from typing import List

from pyautoeios import hooks
from pyautoeios.rs_node import RSNode
from pyautoeios.rs_structures import RSType


class RSHashTable(RSType):
    def head(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.HASHTABLE_HEAD)
        return RSNode(self.eios, _ref)

    def tail(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.HASHTABLE_TAIL)
        return RSNode(self.eios, _ref)

    def bucket(self, index: int) -> RSNode:
        raise NotImplementedError

    def buckets(self) -> List[RSNode]:
        raise NotImplementedError

    def index(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.HASHTABLE_INDEX)

    def size(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.HASHTABLE_SIZE)

    def get_object(self, id: int) -> RSNode:
        raise NotImplementedError
