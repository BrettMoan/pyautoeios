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
from getpass import getpass

from pyautoeios.rs_player import me

# pylint: disable=protected-access, missing-function-docstring

PLAYER_NAME = os.environ.get("PLAYER_NAME", None)
if not PLAYER_NAME:
    PLAYER_NAME = getpass(prompt="enter expected username:")

def test_rs_player_me(client):
    local_player = me(client)
    assert PLAYER_NAME == local_player.name()
