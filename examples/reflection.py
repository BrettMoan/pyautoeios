import ctypes
import pyautoeios as pyauto
from pyautoeios import hooks

from pyautoeios.rs_player import me

from pyautoeios.rs_client import RSClient

pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)
# print(f"{client = }")
# local_player = me(client)
# print(f"{local_player = }")
# name = local_player.name()
# print(f"{name = }")

# for skill_name in local_player.SKILL_KEYS.keys():
#     level = local_player.level(skill_name)
#     max_level = local_player.max_level(skill_name)
#     experience = local_player.experience(skill_name)
#     print(f"{skill_name}: {level = }, {max_level = }, {experience = }")


rs_client = RSClient(client, None)

# is_menu_open = rs_client.is_menu_open()
# print(f"{is_menu_open = }")
# if is_menu_open: 
#     menu_bounds = rs_client.menu_bounds()
#     print(f"{menu_bounds = }")

menu_options = rs_client.menu_options()
menu_actions = rs_client.menu_actions()
print(f"{menu_options.size = }")
for i in range(0, menu_options.size):
    action = menu_actions[i]
    option = menu_options[i]
    if action or option:
        print(f"{i = }, {action} {option}")
