# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_structures import RSType


class RSAnimationSkeleton(RSType):
    def id(self) -> int:
        raise NotImplementedError

    def transform_count(self) -> int:
        raise NotImplementedError

    def transformation_types(self) -> List[int]:
        raise NotImplementedError

    def transformation(self, index: int) -> List[int]:
        raise NotImplementedError

    def transformations(self) -> List[List[int]]:
        raise NotImplementedError
