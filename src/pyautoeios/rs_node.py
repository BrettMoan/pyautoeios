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

from pyautoeios.rs_structures import RSType
from pyautoeios import hooks


class RSNode(RSType):
    def uid(self) -> int:
        return self.eios.get_long(self.ref, hooks.NODE_UID)

    def previous(self):
        _ref = self.eios.get_object(self.ref, hooks.NODE_PREV)
        return RSNode(self.eios, _ref)

    def next(self):
        _ref = self.eios.get_object(self.ref, hooks.NODE_NEXT)
        return RSNode(self.eios, _ref)
