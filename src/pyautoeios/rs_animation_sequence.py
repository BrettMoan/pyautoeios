# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_model import RSModel
from pyautoeios.rs_animated_model import RSAnimatedModel
from pyautoeios.rs_structures import RSType


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
