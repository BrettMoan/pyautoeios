# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_structures import RSType, get_rs_int_array
from pyautoeios.rs_animation_skeleton import RSAnimationSkeleton


class RSAnimation(RSType):
    def frame_count(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ANIMATION_FRAMECOUNT)

    def frame(self, index: int) -> int:
        return self.frames()[index]

    def frames(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ANIMATION_FRAMES,
        )

    def transform_x(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ANIMATION_TRANSFORMX,
        )

    def transform_y(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ANIMATION_TRANSFORMY,
        )

    def transform_z(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ANIMATION_TRANSFORMZ,
        )

    def skeleton(self) -> RSAnimationSkeleton:
        _ref = self.eios._Reflect_Object(self.ref, hooks.ANIMATION_SKELETON)
        return RSAnimationSkeleton(self.eios, _ref)
