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

from typing import List, Tuple

from pyautoeios import hooks
from pyautoeios.rs_structures import RSType


class RSModel(RSType):
    def raw_vertices(self) -> List[List[int]]:
        raise NotImplementedError

    def raw_indices(self) -> List[List[int]]:
        raise NotImplementedError

    def vertices(self) -> List[Tuple[int, int, int]]:
        raise NotImplementedError

    def indices(self) -> List[Tuple[int, int, int]]:
        raise NotImplementedError

    def triangle_faces(self) -> List[Tuple[int, int, int]]:
        raise NotImplementedError

    def skin(self, Index: int) -> List[int]:
        raise NotImplementedError

    def skins(self) -> List[List[int]]:
        raise NotImplementedError

    def fits_single_tile(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.MODEL_FITSSINGLETILE)

    def height(self) -> int:
        return self.eios.get_int(self.ref, hooks.RENDERABLE_MODELHEIGHT)

    def bounds(
        self, local_x: int, local_y: int, local_z: int
    ) -> List[Tuple[int, int, int]]:
        raise NotImplementedError

    def scale(self, scales: Tuple[int, int, int]) -> List[List[int]]:
        raise NotImplementedError
