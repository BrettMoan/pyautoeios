from pyautoeios import hooks
from pyautoeios.rs_structures import RSType, get_rs_int_array


class RSVarps(RSType):
    def varp_mask(self, index: int) -> int:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.VARPS_MASKS,
        )

    def varp_main(self, index: int) -> int:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.VARPS_MAIN,
        )
