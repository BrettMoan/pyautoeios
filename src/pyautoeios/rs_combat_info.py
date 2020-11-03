from pyautoeios import hooks
from pyautoeios.rs_node import RSNode
from pyautoeios.rs_structures import RSType


class RSCombatInfoList(RSType):
    def head(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.COMBATINFOLIST_HEAD)
        return RSNode(self.eios, _ref)


class RSCombatInfo(RSType):
    def health(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.COMBATINFO1_HEALTH)

    def health_ratio(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.COMBATINFO1_HEALTHRATIO)

    def health_scale(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.COMBATINFO2_HEALTHSCALE)
