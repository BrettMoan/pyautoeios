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

# import ctypes
# from pyautoeios import hooks

import pyautoeios as pyauto
from pyautoeios._internal.rs_player import me

# from pyautoeios._internal.rs_client import RSClient

pyauto.inject_clients()
with pyauto.clients.pop(0) as client:
    pyauto.pair_client(client)
    local_player = me(client)
    # name = local_player.name()
    print(f"{client = }, {local_player = }")
    for skill_name in local_player.SKILL_KEYS.keys():
        level = local_player.level(skill_name)
        max_level = local_player.max_level(skill_name)
        experience = local_player.experience(skill_name)
        print(f"{skill_name}: {level = }, {max_level = }, {experience = }")


# rs_client = RSClient(client, None)
# indices = rs_client.npc_indices()
# print([i for i in indices if i])

# is_menu_open = rs_client.is_menu_open()
# print(f"{is_menu_open = }")
# if is_menu_open:
#     menu_bounds = rs_client.menu_bounds()
#     print(f"{menu_bounds = }")

# menu_options = rs_client.menu_options()
# menu_actions = rs_client.menu_actions()
# print(f"{menu_options.size = }")
# print(f"{menu_actions = }")
# print(f"{menu_options = }")
