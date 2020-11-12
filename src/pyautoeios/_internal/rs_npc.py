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

from typing import List

from pyscreeze import Point

from pyautoeios import hooks
from pyautoeios._internal.rs_actor import RSActor
from pyautoeios._internal.rs_model import RSModel
from pyautoeios._internal.rs_npc_definition import RSNPCDefinition
from pyautoeios._internal.rs_animated_model import RSAnimatedModel


class RSNPC(RSActor):
    def definition(self) -> RSNPCDefinition:
        _ref = self.eios.get_object(self.ref, hooks.NPC_DEFINITION)
        return RSNPCDefinition(self.eios, _ref)

    def all_npcs(self):
        raise NotImplementedError(
            "moved to RSClient in python verison, to prevent circular imports"
        )

    def model(self) -> RSModel:
        raise NotImplementedError

    def animated_model(self) -> RSAnimatedModel:
        raise NotImplementedError

    def to_tpa(self) -> List[Point]:
        raise NotImplementedError
