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
from pyautoeios.rs_structures import RSType, get_rs_int_array
from pyautoeios.rs_animation_skeleton import RSAnimationSkeleton


class RSAnimation(RSType):
    def frame_count(self) -> int:
        return self.eios.get_int(self.ref, hooks.ANIMATION_FRAMECOUNT)

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
        _ref = self.eios.get_object(self.ref, hooks.ANIMATION_SKELETON)
        return RSAnimationSkeleton(self.eios, _ref)
