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

import ctypes
import pyautoeios as pyauto
from pyautoeios._internal import hooks
from pyautoeios._internal.rs_client import RSClient

pyauto.inject_clients()
client = pyauto.clients[0]
rs_client = RSClient(client, None)

menu_options = rs_client.menu_options()
menu_actions = rs_client.menu_actions()
print(f"{len(menu_options) = }")
# print all the menu actions
joined_and_filtered = [
    " ".join(str(item)).strip()
    for item in zip(menu_actions, menu_options)
    if item[0] or item[1]
]
print(f"{len(joined_and_filtered) = } ")
print(joined_and_filtered)
