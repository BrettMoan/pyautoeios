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

# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios import static
from pyautoeios._internal.rs_structures import RSType
from pyautoeios._internal.rs_object import RSObject, RSObjectType


class RSSceneTile(RSType):
    def boundary_object(self) -> RSObject:
        _ref = self.eios.get_object(self.ref, hooks.SCENETILE_BOUNDARYOBJECT)
        return RSObject(self.eios, _ref, RSObjectType.BOUNDARY_OBJECT)

    def scene_tile_object(self) -> RSSceneTile:
        _ref = self.eios.get_object(self.ref, hooks.SCENETILE_SCENETILEOBJECT)
        return RSSceneTile(self.eios, _ref)

    def game_object(self) -> RSObject:
        raise NotImplementedError

    def game_objects(self) -> List[RSObject]:
        raise NotImplementedError

    def wall_decoration(self) -> RSObject:
        _ref = self.eios.get_object(self.ref, hooks.SCENETILE_WALLDECORATION)
        return RSObject(self.eios, _ref, RSObjectType.WALL_DECORATION)

    def ground_decoration(self) -> RSObject:
        _ref = self.eios.get_object(self.ref, hooks.SCENETILE_GROUNDDECORATION)
        return RSObject(self.eios, _ref, RSObjectType.FLOOR_DECORATION)

    def local_x(self) -> int:
        return self.eios.get_int(self.ref, hooks.SCENETILE_LOCALX)

    def local_y(self) -> int:
        return self.eios.get_int(self.ref, hooks.SCENETILE_LOCALY)

    def plane(self) -> int:
        return self.eios.get_int(self.ref, hooks.SCENETILE_PLANE)
