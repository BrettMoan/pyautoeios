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

# annotations delays checking of type annotation in pytthon 3.7->3.9
# this will become the default in python 3.10
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations

from pyautoeios._internal import hooks
from pyautoeios._internal.rs_structures import RSType


class RSNameInfo(RSType):
    def name(self):
        return self.eios.get_string(self.ref, hooks.NAMEINFO_NAME).replace(
            "\xa0", " "
        )  # replace nbsp with space

    def decoded_name(self):
        return self.eios.get_string(self.ref, hooks.NAMEINFO_DECODEDNAME).replace(
            "\xa0", " "
        )  # replace nbsp with space
