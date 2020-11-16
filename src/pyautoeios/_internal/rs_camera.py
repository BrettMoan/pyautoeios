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

from pyautoeios._internal import hooks
from pyautoeios._internal.rs_structures import RSType


class RSCamera(RSType):
    def x(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_CAMERAX)

    def y(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_CAMERAY)

    def z(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_CAMERAZ)

    def pitch(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_CAMERAPITCH)

    def yaw(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_CAMERAYAW)
