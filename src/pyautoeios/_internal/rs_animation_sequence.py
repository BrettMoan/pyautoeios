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
from typing import List

from pyautoeios import hooks
from pyautoeios._internal.rs_animated_model import RSAnimatedModel
from pyautoeios._internal.rs_cache import RSCache
from pyautoeios._internal.rs_model import RSModel
from pyautoeios._internal.rs_structures import RSType


class RSAnimationSequence(RSType):
    def frame(self, index: int) -> int:
        raise NotImplementedError

    def frames(self) -> List[int]:
        raise NotImplementedError

    def animation_sequence_cache(self) -> RSCache:
        raise NotImplementedError

    def frame_cache(self) -> RSCache:
        raise NotImplementedError

    def transform_actor_model(
        self,
        model: RSModel,
        frame_id: int,
    ) -> RSAnimatedModel:
        raise NotImplementedError

    def transform_object_model(
        self,
        model: RSModel,
        frame_id: int,
    ) -> RSAnimatedModel:
        raise NotImplementedError

    def apply_transformations(
        self,
        model: RSModel,
        idle_frame_id: int,
        AnimationSequence: RSAnimationSequence,
        movement_frame_id: int,
    ) -> RSAnimatedModel:
        raise NotImplementedError
