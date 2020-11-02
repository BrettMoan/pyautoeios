from typing import Type

from pyscreeze import Point

from pyautoeios import hooks
from pyautoeios import static
from pyautoeios.eios import EIOS
from pyautoeios.rs_structures import RSType




class RSTile(RSType):
    def __init__(self, eios:EIOS, x:int, y:int):
        self.x = x
        self.y = y
        super().__init__(eios=eios, ref=None)

    def region_id(self) -> int:
        return ((self.x >> 6) << 8) or (self.y >> 6)

    def to_local(self) -> Type[RSTile]:
        x = ((self.x - static.base_x(self.eios)) << 7) + (1 << 6)
        y = ((self.y - static.base_y(self.eios)) << 7) + (1 << 6)
        return RSTile(self.eios, x, y)

    def to_global(self) -> Type[RSTile]:
        x = static.base_x(self.eios) + self.x // 128
        y = static.base_y(self.eios) + self.y // 128
        return RSTile(self.eios, x, y)

    def local_to_world_tile(self) -> Type[RSTile]:
        raise NotImplementedError

    def world_to_local_tile(self) -> Type[RSTile]:
        raise NotImplementedError

    def tile_to_mm(self) -> Point:
        raise NotImplementedError

    def mm_to_tile(self) -> Type[RSTile]:
        raise NotImplementedError

    def tile_to_ms(self) -> Point:
        raise NotImplementedError

    def get_height(self, plane: int=None) -> int:
        raise NotImplementedError
