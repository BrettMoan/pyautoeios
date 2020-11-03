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
        return self.eios._Reflect_Bool(self.ref, hooks.MODEL_FITSSINGLETILE)

    def height(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.RENDERABLE_MODELHEIGHT)

    def bounds(
        self, local_x: int, local_y: int, local_z: int
    ) -> List[Tuple[int, int, int]]:
        raise NotImplementedError

    def scale(self, scales: Tuple[int, int, int]) -> List[List[int]]:
        raise NotImplementedError
