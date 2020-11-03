from pyautoeios import hooks
from pyautoeios.rs_queue import RSQueue
from pyautoeios.rs_structures import RSType
from pyautoeios.rs_iterable_hash_table import RSIterableHashTable


class RSCache(RSType):
    def hash_table(self) -> RSIterableHashTable:
        _ref = self.eios._Reflect_Object(self.ref, hooks.CACHE_HASHTABLE)
        return RSIterableHashTable(self.eios, _ref)

    def queue(self) -> RSQueue:
        _ref = self.eios._Reflect_Object(self.ref, hooks.CACHE_QUEUE)
        return RSQueue(self.eios, _ref)

    def remaining(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.CACHE_REMAINING)

    def capacity(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.CACHE_CAPACITY)
