from typing import List

from pyautoeios import hooks
from pyautoeios.rs_node import RSNode
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_model import RSModel
from pyautoeios.rs_structures import RSType, get_rs_int_array
from pyautoeios.rs_animated_model import RSAnimatedModel
from pyautoeios.rs_animation_sequence import RSAnimationSequence


class RSPlayerDefinition(RSType):
    def id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.PLAYERDEFINITION_NPCTRANSFORMID)

    def is_female(self) -> bool:
        return self.eios._Reflect_Bool(None, hooks.PLAYERDEFINITION_ISFEMALE)

    def model_id(self) -> int:
        return self.eios._Reflect_Long(self.ref, hooks.PLAYERDEFINITION_MODELID)

    def animated_model_id(self) -> int:
        return self.eios._Reflect_Long(self.ref, hooks.PLAYERDEFINITION_ANIMATEDMODELID)

    def equipment(self) -> List[int]:
        return get_rs_int_array(self.eios, ref=self.ref, hook=hooks.PLAYERDEFINITION_EQUIPMENT)

    def model_cache(self) -> RSCache:
        _ref = self.eios._Reflect_Object(self.ref, hooks.NPCDEFINITION_MODELCACHE)
        return RSCache(eios=self.eios, ref=_ref)

    def cached_model(self) -> RSModel:
        raise NotImplementedError

    def get_model(self, model: RSModel, idle_sequence: RSAnimationSequence, animation_frame: int, movement_sequence: RSAnimationSequence, movement_frame: int) -> RSAnimatedModel:
        raise NotImplementedError
