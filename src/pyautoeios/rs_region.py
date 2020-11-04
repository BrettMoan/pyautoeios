from typing import List, TypeVar

from pyautoeios import hooks
from pyautoeios.rs_object import RSObject
from pyautoeios.rs_structures import RSType
from pyautoeios.rs_scene_tile import RSSceneTile


Scene = List[List[RSSceneTile]]
S = TypeVar("S", Scene, List[Scene])


class RSRegion(RSType):
    def scene_tiles(self, plane: int) -> S:
        raise NotImplementedError

    def scene_tile(self, x: int, y: int, z: int) -> RSSceneTile:
        raise NotImplementedError

    def interactable_objects(self) -> List[RSObject]:
        raise NotImplementedError
