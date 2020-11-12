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

import random
import getpass
from pyscreeze import Box
import pyautoeios as pyauto


pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    pyauto.static.move_to_spot_in_box(Box(left=398, top=271, width=148, height=40))
    pyauto.static.click_on_spot_in_box(Box(left=285, top=248, width=235, height=15))
    pyauto.typewrite(getpass.getpass(), interval=0.7)
    im = pyauto.screenshot()
    im.show()
    pyauto.static.click_on_spot_in_box(Box(left=238, top=301, width=148, height=41))
