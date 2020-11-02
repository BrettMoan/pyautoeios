from pyautoeios.eios import EIOS, ReflectionArrayType
from pyautoeios.rs_structures import RSType, RSIntArray
from pyautoeios import hooks


class RSPlayer(RSType):
    def name(self):
        _ref = self.eios._Reflect_Object(self.ref, hooks.PLAYER_NAME)
        name_info = RSNameInfo(self.eios, _ref)
        name = name_info.name().replace(b"\xc2\xa0", b" ")  # replace nbsp with space
        return name


class RSNameInfo(RSType):
    def name(self):
        return self.eios._Reflect_String(self.ref, hooks.NAMEINFO_NAME)


class RSLocalPlayer(RSPlayer):
    SKILL_KEYS = {
        "ATTACK": 0,
        "DEFENCE": 1,
        "STRENGTH": 2,
        "HITPOINTS": 3,
        "RANGED": 4,
        "PRAYER": 5,
        "MAGIC": 6,
        "COOKING": 7,
        "WOODCUTTING": 8,
        "FLETCHING": 9,
        "FISHING": 10,
        "FIREMAKING": 11,
        "CRAFTING": 12,
        "SMITHING": 13,
        "MINING": 14,
        "HERBLORE": 15,
        "AGILITY": 16,
        "THIEVING": 17,
        "SLAYER": 18,
        "FARMING": 19,
        "RUNECRAFT": 20,
        "HUNTER": 21,
        "CONSTRUCTION": 22,
        # 'TOTALLEVEL' : 23, # broken, returns a 1.
    }

    # def __init__(self, eios: EIOS = None, ref=None):
    #     super().__init__(eios, ref)
    #     self._currentlevels = None
    #     self._reallevels = None
    #     self._experiences = None
    # def __del__(self):
    #     del self._currentlevels
    #     del self._reallevels
    #     del self._experiences
    #     super().__del__()
    # def _get_skills_array()

    def _get_skill_int(self, skill_name: str, hook: hooks.THook) -> int:
        index = self.SKILL_KEYS[skill_name]
        _ref = self.eios._Reflect_Array(None, hook)
        skills_array = RSIntArray(self.eios, _ref)
        return skills_array[index]

    def level(self, skill_name: str) -> int:
        return self._get_skill_int(skill_name, hooks.CLIENT_CURRENTLEVELS)

    def max_level(self, skill_name: str) -> int:
        return self._get_skill_int(skill_name, hooks.CLIENT_REALLEVELS)

    def experience(self, skill_name: str) -> int:
        return self._get_skill_int(skill_name, hooks.CLIENT_EXPERIENCES)


def me(eios: EIOS):
    return RSLocalPlayer(eios, eios._Reflect_Object(None, hooks.CLIENT_LOCALPLAYER))
