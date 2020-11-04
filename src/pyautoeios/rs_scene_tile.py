# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios import static
from pyautoeios.rs_structures import RSType
from pyautoeios.rs_object import RSObject, RSObjectType


class RSSceneTile(RSType):
    def boundary_object(self) -> RSObject:
        _ref = self.eios._Reflect_Object(self.ref, hooks.SCENETILE_BOUNDARYOBJECT)
        return RSObject(self.eios, _ref, RSObjectType.BOUNDARY_OBJECT)

    def scene_tile_object(self) -> RSSceneTile:
        _ref = self.eios._Reflect_Object(self.ref, hooks.SCENETILE_SCENETILEOBJECT)
        return RSSceneTile(self.eios, _ref)

    def game_object(self) -> RSObject:
        raise NotImplementedError

    def game_objects(self) -> List[RSObject]:
        raise NotImplementedError

    def wall_decoration(self) -> RSObject:
        _ref = self.eios._Reflect_Object(self.ref, hooks.SCENETILE_WALLDECORATION)
        return RSObject(self.eios, _ref, RSObjectType.WALL_DECORATION)

    def ground_decoration(self) -> RSObject:
        _ref = self.eios._Reflect_Object(self.ref, hooks.SCENETILE_GROUNDDECORATION)
        return RSObject(self.eios, _ref, RSObjectType.FLOOR_DECORATION)

    def local_x(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.SCENETILE_LOCALX)

    def local_y(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.SCENETILE_LOCALY)

    def plane(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.SCENETILE_PLANE)
