from typing import List, Tuple

from pyautoeios import hooks
from pyautoeios.rs_structures import RSType

class RSModel(RSType):
    def raw_vertices(self) -> List[List[int]]:
        raise NotImplementedError

    def raw_indices(self) -> List[List[int]]:
        raise NotImplementedError

    def vertices(self) ->List[Tuple[int,int,int]]:
        raise NotImplementedError

    def indices(self) ->List[Tuple[int,int,int]]:
        raise NotImplementedError

    def triangle_faces(self) ->List[Tuple[int,int,int]]:
        raise NotImplementedError

    def skin(self, Index: int) -> List[int]:
        raise NotImplementedError

    def skins(self) -> List[List[int]]:
        raise NotImplementedError

    def fits_single_tile(self) -> bool:
        raise NotImplementedError

    def height(self) -> int:
        raise NotImplementedError

    def bounds(self, local_x: int, local_y: int, local_z: int) -> List[Tuple[int,int,int]]:
        raise NotImplementedError

    def scale(self, scales: Tuple[int,int,int]) -> List[List[int]]:
        raise NotImplementedError
