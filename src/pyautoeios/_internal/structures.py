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


from dataclasses import dataclass

from pyscreeze import Point

# pylint: disable=invalid-name

@dataclass(frozen=True)
class TVector:
    __slots__ = ["x", "y", "z"]
    x: int
    y: int
    z: int

@dataclass(frozen=True)
class TTriangle:
    __slots__ = ["a", "b", "c"]
    a: TVector
    b: TVector
    c: TVector

#
@dataclass(frozen=True)
class T2DTriangle:
    __slots__ = ["a", "b", "c"]
    a: Point
    b: Point
    c: Point


@dataclass(frozen=True)
class T2DRectangle:
    __slots__ = ["nw", "ne", "sw", "se"]
    nw: Point
    ne: Point
    sw: Point
    se: Point
