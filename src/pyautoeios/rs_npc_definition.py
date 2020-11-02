from typing import List, Tuple


from pyautoeios import hooks
from pyautoeios.rs_region import RSRegion
from pyautoeios.rs_model import RSModel
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_structures import RSType, RSIntArray, RSStringArray, get_rs_int_array
from pyautoeios.rs_animated_model import RSAnimatedModel
from pyautoeios.rs_animation_sequence import RSAnimationSequence

class RSNPCDefinition(RSType):
    def id(self):
        return self.eios._Reflect_Int(self.ref, hooks.NPCDEFINITION_ID)

    def name(self):
        return self.eios._Reflect_String(self.ref, hooks.NPCDEFINITION_NAME).decode("utf8")

    def actions(self) -> List[str]:
        return get_rs_int_array(self.eios, ref=None, hook=hooks.NPCDEFINITION_ACTIONS)

    def model_ids(self) -> List[int]:
        return get_rs_int_array(self.eios, ref=None, hook=hooks.NPCDEFINITION_MODELIDS)

    def combat_level(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.NPCDEFINITION_COMBATLEVEL)

    def is_visible(self) -> bool:
        return self.eios._Reflect_Bool(self.ref, hooks.NPCDEFINITION_VISIBLE)

    def transformations(self) -> List[int]:
        return get_rs_int_array(self.eios, ref=None, hook=hooks.NPCDEFINITION_TRANSFORMATIONS)

    def model_tile_size(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.NPCDEFINITION_MODELTILESIZE)

    def model_scale(self) -> Tuple[int,int,int]:
          x = self.eios._Reflect_Int(self.ref, hooks.NPCDEFINITION_MODELSCALEWIDTH)
          y = self.eios._Reflect_Int(self.ref, hooks.NPCDEFINITION_MODELSCALEHEIGHT)
          z = x
          return (x, y, z)

    def model_cache(self) -> RSCache:
        _ref = self.eios._Reflect_Object(self.ref, hooks.NPCDEFINITION_MODELCACHE)
        return RSCache(eios=self.eios, ref=_ref)

    def cached_model(self) -> RSModel:
        raise NotImplementedError

    def get_model(self, model: RSModel, idle_sequence: RSAnimationSequence, animation_frame: int, movement_sequence: RSAnimationSequence, movement_frame: int) -> RSAnimatedModel:
        raise NotImplementedError
