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

from typing import List, Tuple


from pyautoeios import hooks
from pyautoeios.rs_region import RSRegion
from pyautoeios.rs_model import RSModel
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_structures import (
    RSType,
    RSIntArray,
    RSStringArray,
    get_rs_int_array,
    get_rs_string_array,
)
from pyautoeios.rs_animated_model import RSAnimatedModel
from pyautoeios.rs_animation_sequence import RSAnimationSequence


class RSNPCDefinition(RSType):
    def id(self):
        return self.eios.get_int(self.ref, hooks.NPCDEFINITION_ID)

    def name(self):
        return self.eios.get_string(self.ref, hooks.NPCDEFINITION_NAME)

    def actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.NPCDEFINITION_ACTIONS,
        )

    def model_ids(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.NPCDEFINITION_MODELIDS,
        )

    def combat_level(self) -> int:
        return self.eios.get_int(self.ref, hooks.NPCDEFINITION_COMBATLEVEL)

    def is_visible(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.NPCDEFINITION_VISIBLE)

    def transformations(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.NPCDEFINITION_TRANSFORMATIONS,
        )

    def model_tile_size(self) -> int:
        return self.eios.get_int(self.ref, hooks.NPCDEFINITION_MODELTILESIZE)

    def model_scale(self) -> Tuple[int, int, int]:
        x = self.eios.get_int(self.ref, hooks.NPCDEFINITION_MODELSCALEWIDTH)
        y = self.eios.get_int(self.ref, hooks.NPCDEFINITION_MODELSCALEHEIGHT)
        z = x
        return (x, y, z)

    def model_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.NPCDEFINITION_MODELCACHE)
        return RSCache(eios=self.eios, ref=_ref)

    def cached_model(self) -> RSModel:
        raise NotImplementedError

    def get_model(
        self,
        model: RSModel,
        idle_sequence: RSAnimationSequence,
        animation_frame: int,
        movement_sequence: RSAnimationSequence,
        movement_frame: int,
    ) -> RSAnimatedModel:
        raise NotImplementedError
