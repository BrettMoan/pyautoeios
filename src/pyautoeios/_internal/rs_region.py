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

from typing import List, TypeVar

from pyautoeios import hooks
from pyautoeios._internal.rs_object import RSObject
from pyautoeios._internal.rs_structures import RSType
from pyautoeios._internal.rs_scene_tile import RSSceneTile


Scene = List[List[RSSceneTile]]
S = TypeVar("S", Scene, List[Scene])


class RSRegion(RSType):
    def scene_tiles(self, plane: int) -> S:
        raise NotImplementedError

    def scene_tile(self, x: int, y: int, z: int) -> RSSceneTile:
        raise NotImplementedError

    def interactable_objects(self) -> List[RSObject]:
        raise NotImplementedError
