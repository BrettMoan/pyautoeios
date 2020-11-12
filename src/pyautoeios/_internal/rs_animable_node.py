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
from pyautoeios import hooks

from pyautoeios._internal.rs_animation_sequence import RSAnimationSequence
from pyautoeios._internal.rs_client import RSClient
from pyautoeios._internal.rs_structures import RSType
from pyautoeios._internal.rs_tile import RSTile


class RSAnimableNode(RSType):
    def id(self) -> int:
        return self.eios.get_int(self.ref, hooks.ANIMABLENODE_ID)

    def animation_sequence(self) -> RSAnimationSequence:
        _ref = self.eios.get_object(self.ref, hooks.ANIMABLENODE_ANIMATIONSEQUENCE)
        return RSAnimationSequence(self.eios, _ref)

    def animation_frame_id(self) -> int:
        return self.id()

    def flags(self) -> int:
        return self.eios.get_int(self.ref, hooks.ANIMABLENODE_FLAGS)

    def orientation(self) -> int:
        return self.eios.get_int(self.ref, hooks.ANIMABLENODE_ORIENTATION)

    def plane(self) -> int:
        return self.eios.get_int(self.ref, hooks.ANIMABLENODE_PLANE)

    def local_x(self) -> int:
        x = self.eios.get_int(self.ref, hooks.ANIMABLENODE_X)
        return (x << 7) + (1 << 6)

    def local_y(self) -> int:
        y = self.eios.get_int(self.ref, hooks.ANIMABLENODE_Y)
        return (y << 7) + (1 << 6)

    def local_tile(self) -> RSTile:
        x = self.local_x()
        y = self.local_y()
        return RSTile(self.eios, x, y)

    def tile(self) -> RSTile:
        client = RSClient(self.eios, None)
        x = client.base_x() + self.eios.get_int(self.ref, hooks.ANIMABLENODE_X)
        y = client.base_y() + self.eios.get_int(self.ref, hooks.ANIMABLENODE_Y)
        return RSTile(self.eios, x, y)
