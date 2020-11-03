import collections
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_tile import RSTile
from pyautoeios.rs_structures import RSType

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
