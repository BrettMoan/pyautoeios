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
from pyautoeios._internal.rs_animated_model import RSAnimatedModel
from pyautoeios._internal.rs_model import RSModel
from pyautoeios._internal.rs_name_info import RSNameInfo
from pyautoeios._internal.rs_player_definition import RSPlayerDefinition
from pyautoeios._internal.rs_actor import RSActor
from pyautoeios._internal.rs_tile import RSTile

class RSPlayer(RSActor):
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
        return self.definition().cached_model()

    def animated_model(self) -> RSAnimatedModel:
        raise NotImplementedError
