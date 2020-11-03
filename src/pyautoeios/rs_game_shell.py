from pyautoeios import hooks
from pyautoeios.rs_structures import RSType
from pyautoeios.rs_varbit_definition import RSVarbitDefinition


class RSGameShell(RSType):
    def get_var_bit(self, id: int) -> int:
        raise NotImplementedError
