from pyautoeios import hooks
from pyautoeios.rs_structures import RSType
from pyautoeios.rs_item_definition import RSItemDefinition


class RSItem(RSType):
    def id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ITEM_ID)

    def stack_sizes(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ITEM_STACKSIZES)

    def definition(self) -> RSItemDefinition:
        raise NotImplementedError
