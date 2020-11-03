# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_structures import RSType
from pyautoeios.rs_animation import RSAnimation


class RSAnimationFrame(RSType):
    def animation(self, index: int) -> RSAnimation:
        raise NotImplementedError

    def animations(self) -> List[RSAnimation]:
        raise NotImplementedError

    def get_frame(self, frame_id: int) -> RSAnimationFrame:
        raise NotImplementedError
