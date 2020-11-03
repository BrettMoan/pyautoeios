from typing import List
from pyautoeios import hooks
from pyautoeios.rs_hash_table import RSHashTable
from pyautoeios.rs_structures import RSType, get_rs_int_array


class RSItemNode(RSType):
    def item_ids(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMNODE_ITEMIDS,
        )

    def item_quantities(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMNODE_ITEMQUANTITIES,
        )

    def hash_table(self) -> RSHashTable:
        _ref = self.eios._Reflect_Object(None, hooks.ITEMNODE_CACHE)
        return RSHashTable(self.eios, _ref)
