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

from pyautoeios._internal import hooks
from pyautoeios.eios import EIOS
from pyautoeios._internal.rs_player import RSPlayer
from pyautoeios._internal.rs_structures import RSIntArray

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

    def __init__(self, eios: EIOS = None) -> RSLocalPlayer:
        _ref = eios.get_object(None, hooks.CLIENT_LOCALPLAYER)
        super().__init__(eios, _ref)

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
