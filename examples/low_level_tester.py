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

import os
import getpass
import random
import time
from pyautoeios.eios import EIOS
from pyautoeios.hexcodes import VK_ESC, VK_LBUTTON

print("injecting into client")
# Create instance of Remote Input
reflect = EIOS()

# Pair the client and get the target or eios_ptr
print(f"client object is = {reflect}")

reflect.lose_focus()
have_focus1 = reflect.has_focus()
print(f"have_focus1 = {have_focus1}")

reflect.gain_focus()
have_focus2 = reflect.has_focus()
print(f"have_focus2 = {have_focus2}")

dimensions = reflect.get_target_dimensions()
print(f"dimensions = {dimensions}")

mouse_position = reflect.get_mouse_position()
print(f"mouse_position = {mouse_position}")

real_mouse_position = reflect.get_real_mouse_position()
print(f"real_mouse_position = {real_mouse_position}")

print(
    "If you're at the login screen enter password to do a stupidly simple login script with fixed coordinates"
)

PLAYER_PASSWORD = os.environ.get("PLAYER_PASSWORD", None)
if not PLAYER_PASSWORD:
    PLAYER_PASSWORD = getpass.getpass(prompt="enter password:")

if PLAYER_PASSWORD:
    reflect.hold_key(VK_ESC)
    time.sleep(0.1 + random.random())
    reflect.release_key(VK_ESC)
    reflect.hold_key(VK_ESC)
    time.sleep(0.1 + random.random())
    reflect.release_key(VK_ESC)
    reflect.hold_key(VK_ESC)
    time.sleep(0.1 + random.random())
    reflect.release_key(VK_ESC)


    x,y = random.randint(473,485), random.randint(280,300)
    reflect.move_mouse(x, y)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

    reflect.hold_mouse(x, y, VK_LBUTTON)
    time.sleep(0.1 + random.random())
    reflect.release_mouse(x, y, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

    x,y = random.randint(365,385), random.randint(253,263)
    reflect.hold_mouse(x, y, VK_LBUTTON)
    time.sleep(0.1 + random.random())
    reflect.release_mouse(x, y, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

    reflect.send_string(PLAYER_PASSWORD, 100, 100)

    x,y = random.randint(320,329), random.randint(310,319)
    reflect.hold_mouse(x, y, VK_LBUTTON)
    time.sleep(0.1 + random.random())
    reflect.release_mouse(x, y, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

reflect.lose_focus()
