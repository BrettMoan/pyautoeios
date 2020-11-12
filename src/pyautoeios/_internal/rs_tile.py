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

from pyscreeze import Point

from pyautoeios import hooks
from pyautoeios import static
from pyautoeios.eios import EIOS
from pyautoeios._internal.rs_structures import RSType


class RSTile(RSType):
    def __init__(self, eios: EIOS, x: int, y: int):
        self.x = x
        self.y = y
        super().__init__(eios=eios, ref=None)

    def region_id(self) -> int:
        return static.shl(static.shr(self.x, 6), 8) or (self.y >> 6)

    def to_local(self) -> RSTile:
        x = ((self.x - static.base_x(self.eios)) << 7) + (1 << 6)
        y = ((self.y - static.base_y(self.eios)) << 7) + (1 << 6)
        return RSTile(self.eios, x, y)

    def to_global(self) -> RSTile:
        x = static.base_x(self.eios) + self.x // 128
        y = static.base_y(self.eios) + self.y // 128
        return RSTile(self.eios, x, y)

    def local_to_world_tile(self) -> RSTile:
        raise NotImplementedError

    def world_to_local_tile(self) -> RSTile:
        raise NotImplementedError

    def tile_to_mm(self) -> Point:
        raise NotImplementedError

    def mm_to_tile(self) -> RSTile:
        raise NotImplementedError

    def tile_to_ms(self) -> Point:
        raise NotImplementedError

    def get_height(self, plane: int = None) -> int:
        raise NotImplementedError
