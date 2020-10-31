import ctypes
import pyautoeios as pyauto
from pyautoeios import hooks

from pyautoeios.rs_player import me

pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)
print(f"{client = }")
local_player = me(client)
print(f"{local_player = }")
name = local_player.name()
print(f"{name = }")

for skill_name in local_player.SKILL_KEYS.keys():
    level = local_player.level(skill_name)
    max_level = local_player.max_level(skill_name)
    experience = local_player.experience(skill_name)
    print(f"{skill_name}: {level = }, {max_level = }, {experience = }")
