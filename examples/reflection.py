import ctypes
import pyautoeios as pyauto
from pyautoeios import hooks

from pyautoeios.rs_player import me

from pyautoeios.rs_client import RSClient

pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)
local_player = me(client)
name = local_player.name()
print(f"{client = }, {local_player = }, {name = }")

# for skill_name in local_player.SKILL_KEYS.keys():
#     level = local_player.level(skill_name)
#     max_level = local_player.max_level(skill_name)
#     experience = local_player.experience(skill_name)
#     print(f"{skill_name}: {level = }, {max_level = }, {experience = }")


rs_client = RSClient(client, None)
indices = rs_client.npc_indices()
print([i for i in indices if i])

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
