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

from pyautoeios._internal import hooks
from pyautoeios.eios import EIOS
from pyautoeios._internal import static
from pyautoeios._internal.rs_structures import RSType, get_rs_int_array, get_rs_string_array
from pyautoeios._internal.rs_cache import RSCache
from pyautoeios._internal.rs_model import RSModel
from pyautoeios._internal.rs_animated_model import RSAnimatedModel


class RSObjectType(Enum):
    GAME_OBJECT = auto()
    WALL_DECORATION = auto()
    BOUNDARY_OBJECT = auto()
    FLOOR_DECORATION = auto()


class RSObjectDefinition(RSType):
    def oid(self) -> int:
        return self.eios.get_int(self.ref, hooks.OBJECTDEFINITION_ID)

    def model_ids(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.OBJECTDEFINITION_MODELIDS,
        )

    def models(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.OBJECTDEFINITION_MODELS,
        )

    def has_models(self) -> bool:
        return len(self.models()) > 0

    def name(self) -> str:
        return self.eios.get_string(self.ref, hooks.OBJECTDEFINITION_NAME)

    def actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.OBJECTDEFINITION_ACTIONS,
        )

    def transformations(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.OBJECTDEFINITION_TRANSFORMATIONS,
        )

    def has_transformations(self) -> bool:
        return len(self.transformations()) > 0

    def definition_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.OBJECTDEFINITION_DEFINITIONCACHE)
        return RSCache(self.eios, _ref)

    def model_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.OBJECTDEFINITION_MODELCACHE)
        return RSCache(self.eios, _ref)

    def definition(self, oid: int) -> RSObjectDefinition:
        cache = self.definition_cache()

        if not cache.ref:
            return None

        hash_table = cache.hash_table()

        if not hash_table.ref:
            return None

        return RSObjectDefinition(
            eios=self.eios,
            ref=hash_table.get_object(oid).ref,
        )

    def model(self, oid: int) -> RSModel:
        raise NotImplementedError

    def transform_varbit(self) -> int:
        return self.eios.get_int(self.ref, hooks.OBJECTDEFINITION_TRANSFORMATIONVARBIT)

    def transform_varp(self) -> int:
        return self.eios.get_int(self.ref, hooks.OBJECTDEFINITION_TRANSFORMATIONVARP)

    def transform(self) -> RSObjectDefinition:
        raise NotImplementedError
