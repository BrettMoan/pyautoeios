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

import collections
from typing import List

from pyautoeios import hooks
from pyautoeios._internal.rs_tile import RSTile
from pyautoeios._internal.rs_structures import RSType

RSGroundItem = collections.namedtuple("RSGroundItem", "id stack_size tile")


class RSGroundObject(RSType):
    def get_all(self) -> List[RSGroundItem]:
        raise NotImplementedError

    def get_item_by_id(self, item_id: int) -> List[RSGroundItem]:
        raise NotImplementedError

    def get_tile_by_id(self, item_id: int) -> List[RSTile]:
        raise NotImplementedError

    def get_items_at(self, x: int, y: int) -> List[RSGroundItem]:
        raise NotImplementedError
