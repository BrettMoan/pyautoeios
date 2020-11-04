# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations


from pyautoeios import hooks
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_structures import RSType


class RSVarbitDefinition(RSType):
    def base_var(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.VARBITDEFINITION_BASE)

    def start_bit(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.VARBITDEFINITION_STARTBIT)

    def end_bit(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.VARBITDEFINITION_ENDBIT)

    def definition_cache(self) -> RSCache:
        _ref = self.eios._Reflect_Object(None, hooks.VARBITDEFINITION_CACHE)
        return RSCache(self.eios, _ref)

    def definition(self, id: int) -> RSVarbitDefinition:
        raise NotImplementedError
