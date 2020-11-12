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
        return self.eios.get_int(self.ref, hooks.PLAYERDEFINITION_NPCTRANSFORMID)

    def is_female(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.PLAYERDEFINITION_ISFEMALE)

    def model_id(self) -> int:
        return self.eios.get_long(self.ref, hooks.PLAYERDEFINITION_MODELID)

    def animated_model_id(self) -> int:
        return self.eios.get_long(self.ref, hooks.PLAYERDEFINITION_ANIMATEDMODELID)

    def equipment(self) -> List[int]:
        return get_rs_int_array(
            self.eios, ref=self.ref, hook=hooks.PLAYERDEFINITION_EQUIPMENT
        )

    def model_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.PLAYERDEFINITION_MODELCACHE)
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
