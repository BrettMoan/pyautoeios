# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_structures import RSType, get_rs_string_array


class RSItemDefinition(RSType):
    def id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ITEMDEFINITION_ID)

    def name(self) -> str:
        return self.eios._Reflect_String(self.ref, hooks.ITEMDEFINITION_NAME)

    def is_members(self) -> bool:
        return self.eios._Reflect_Bool(self.ref, hooks.ITEMDEFINITION_ISMEMBERS)

    def actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMDEFINITION_ACTIONS,
        )

    def ground_actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMDEFINITION_GROUNDACTIONS,
        )

    def definition_cache(self) -> RSCache:
        _ref = self.eios._Reflect_Object(None, hooks.ITEMDEFINITION_CACHE)
        return RSCache(self.eios, _ref)

    def get(self, id: int) -> RSItemDefinition:
        raise NotImplementedError
