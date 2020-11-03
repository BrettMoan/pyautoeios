# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from enum import Enum, auto
from __future__ import annotations
from typing import List, Optional, overload, Union

from pyautoeios import hooks
from pyautoeios.eios import EIOS
from pyautoeios import static
from pyautoeios.rs_structures import RSType, get_rs_int_array, get_rs_string_array
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_model import RSModel
from pyautoeios.rs_animated_model import RSAnimatedModel



class RSObjectType(Enum):
    GAME_OBJECT = auto()
    WALL_DECORATION = auto()
    BOUNDARY_OBJECT = auto()
    FLOOR_DECORATION = auto()


class RSObjectDefinition(RSType):
    def id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.OBJECTDEFINITION_ID)

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
        return self.eios._Reflect_String(self.ref, hooks.OBJECTDEFINITION_NAME)

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
        _ref = self.eios._Reflect_Object(None, hooks.OBJECTDEFINITION_DEFINITIONCACHE)
        return RSCache(self.eios, _ref)

    def model_cache(self) -> RSCache:
        _ref = self.eios._Reflect_Object(None, hooks.OBJECTDEFINITION_MODELCACHE)
        return RSCache(self.eios, _ref)

    def definition(self, id: int) -> RSObjectDefinition:
        raise NotImplementedError

    def model(self, id: int) -> RSModel:
        raise NotImplementedError

    def transform_varbit(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.OBJECTDEFINITION_TRANSFORMATIONVARBIT)

    def transform_varp(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.OBJECTDEFINITION_TRANSFORMATIONVARP)

    def transform(self) -> RSObjectDefinition:
        raise NotImplementedError
