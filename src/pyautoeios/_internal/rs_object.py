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
from enum import Enum, auto
from typing import List, Optional, overload, Union

from pyautoeios import hooks
from pyautoeios.eios import EIOS
from pyautoeios import static
from pyautoeios._internal.rs_node import RSNode
from pyautoeios._internal.rs_structures import RSType
from pyautoeios._internal.rs_tile import RSTile
from pyautoeios._internal.rs_object_definition import RSObjectDefinition
from pyautoeios._internal.rs_entity import RSEntity
from pyautoeios._internal.rs_model import RSModel
from pyautoeios._internal.rs_animated_model import RSAnimatedModel


class RSObjectType(Enum):
    GAME_OBJECT = auto()
    WALL_DECORATION = auto()
    BOUNDARY_OBJECT = auto()
    FLOOR_DECORATION = auto()


class RSObject(RSType):
    def __init__(self, eios: EIOS, ref, object_type: RSObjectType):
        self.object_type = object_type
        super().__init__(eios=eios, ref=ref)

    hash_hooks = {
        RSObjectType.GAME_OBJECT: hooks.GAMEOBJECT_ID,
        RSObjectType.WALL_DECORATION: hooks.WALLDECORATION_ID,
        RSObjectType.BOUNDARY_OBJECT: hooks.BOUNDARYOBJECT_ID,
        RSObjectType.FLOOR_DECORATION: hooks.FLOORDECORATION_ID,
    }
    x_hooks = {
        RSObjectType.GAME_OBJECT: hooks.GAMEOBJECT_LOCALX,
        RSObjectType.WALL_DECORATION: hooks.WALLDECORATION_LOCALX,
        RSObjectType.BOUNDARY_OBJECT: hooks.BOUNDARYOBJECT_LOCALX,
        RSObjectType.FLOOR_DECORATION: hooks.FLOORDECORATION_LOCALX,
    }
    y_hooks = {
        RSObjectType.GAME_OBJECT: hooks.GAMEOBJECT_LOCALY,
        RSObjectType.WALL_DECORATION: hooks.WALLDECORATION_LOCALY,
        RSObjectType.BOUNDARY_OBJECT: hooks.BOUNDARYOBJECT_LOCALY,
        RSObjectType.FLOOR_DECORATION: hooks.FLOORDECORATION_LOCALY,
    }

    # two refernces on what @overload does and how it works
    #   https://docs.python.org/3/library/typing.html#typing.overload
    #   https://mypy.readthedocs.io/en/stable/more_types.html?highlight=overload#function-overloading
    @overload
    def get(self, object_type: RSObjectType) -> List[RSObject]:
        ...

    @overload
    def get(self, object_type: RSObjectType, x: int, y: int) -> RSObject:
        ...

    def get(
        self,
        object_type: RSObjectType,
        x: Optional[int] = None,
        y: Optional[int] = None,
    ) -> Union[RSObject, List[RSObject]]:
        raise NotImplementedError

    def hash(self) -> int:
        return self.eios.get_long(self.ref, self.hash_hooks[self.object_type])

    def id(self) -> int:
        """
        TODO
        might need to un-hard-code this from 32, to be architecture agnostic
        the pascal code is
           Result := (self.Hash shr 17) and $FFFFFFFF;
        and $FFFFFFFF might vary by the architecture (32 vs 64 bit)
        """
        raise static.shr(self.hash(), 17) & (2 ** 32 - 1)

    def local_tile(self) -> RSTile:
        x = self.eios.get_int(self.ref, self.x_hooks[self.object_type])
        y = self.eios.get_int(self.ref, self.y_hooks[self.object_type])
        return RSTile(self.eios, x, y)

    def tile(self) -> RSTile:
        local_tile = self.local_tile()
        x = (static.base_x(self.eios) + local_tile.x) // 128
        y = (static.base_y(self.eios) + local_tile.y) // 128
        return RSTile(self.eios, x, y)

    def definition(self) -> RSObjectDefinition:
        raise NotImplementedError

    def renderable(self) -> RSEntity:
        raise NotImplementedError

    def model(self) -> RSModel:
        raise NotImplementedError

    def animated_model(self) -> RSAnimatedModel:
        raise NotImplementedError
