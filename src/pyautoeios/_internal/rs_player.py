#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.

# annotations delays checking of type annotation in pytthon 3.7->3.9
# this will become the default in python 3.10
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations

from pyautoeios import hooks
from pyautoeios.eios import EIOS
from pyautoeios._internal.rs_tile import RSTile
from pyautoeios._internal.rs_model import RSModel
from pyautoeios._internal.rs_structures import RSType, RSIntArray
from pyautoeios._internal.rs_animated_model import RSAnimatedModel
from pyautoeios._internal.rs_player_definition import RSPlayerDefinition


class RSPlayer(RSType):
    def me(self) -> RSLocalPlayer:
        return RSLocalPlayer(
            self.eios, self.eios.get_object(None, hooks.CLIENT_LOCALPLAYER)
        )

    def name(self) -> str:
        _ref = self.eios.get_object(self.ref, hooks.PLAYER_NAME)
        name_info = RSNameInfo(self.eios, _ref)
        name = name_info.name()
        return name

    def all_players(self):
        raise NotImplementedError(
            "moved to RSClient in python verison, to prevent circular imports"
        )

    def is_visible(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.PLAYER_VISIBLE)

    def definition(self) -> RSPlayerDefinition:
        _ref = self.eios.get_object(self.ref, hooks.PLAYER_DEFINITION)
        return RSPlayerDefinition(self.eios, _ref)

    def combat_level(self) -> int:
        return self.eios.get_int(self.ref, hooks.PLAYER_COMBATLEVEL)

    def destination(self) -> RSTile:
        raise NotImplementedError

    def is_moving(self) -> bool:
        return self.eios.get_int(self.ref, hooks.ACTOR_QUEUESIZE) > 0

    def model(self) -> RSModel:
        raise NotImplementedError

    def animated_model(self) -> RSAnimatedModel:
        raise NotImplementedError


class RSNameInfo(RSType):
    def name(self):
        return self.eios.get_string(self.ref, hooks.NAMEINFO_NAME).replace(
            "\xa0", " "
        )  # replace nbsp with space

    def decoded_name(self):
        return self.eios.get_string(self.ref, hooks.NAMEINFO_DECODEDNAME).replace(
            "\xa0", " "
        )  # replace nbsp with space


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
        # 'TOTALLEVEL' : 23, # TODO: broken, returns a 1.
    }

    def index(self) -> int:
        return (
            self.eios.get_int(None, hooks.CLIENT_PLAYERINDEX) + 2 ** 15
        ) % 2 ** 16 - 2 ** 15

    def _get_skill_int(self, skill_name: str, hook: hooks.THook) -> int:
        index = self.SKILL_KEYS[skill_name]
        _ref = self.eios.get_array(None, hook)
        skills_array = RSIntArray(self.eios, _ref)
        return skills_array[index]

    def level(self, skill_name: str) -> int:
        return self._get_skill_int(skill_name, hooks.CLIENT_CURRENTLEVELS)

    def max_level(self, skill_name: str) -> int:
        return self._get_skill_int(skill_name, hooks.CLIENT_REALLEVELS)

    def experience(self, skill_name: str) -> int:
        return self._get_skill_int(skill_name, hooks.CLIENT_EXPERIENCES)

    def current_world(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_CURRENTWORLD)

    def run_energy(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_ENERGY)

    def weight(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_WEIGHT)


def me(eios: EIOS) -> RSLocalPlayer:
    return RSLocalPlayer(eios, eios.get_object(None, hooks.CLIENT_LOCALPLAYER))
