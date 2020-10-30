import pyautoeios as pyauto
from pyautoeios import hooks

from pyautoeios.rs_player import me

pyauto.inject_clients()
client=pyauto.clients[0]
pyauto.pair_client(client)
print(f"{client = }")

print(client._Reflect_Int(None, hooks.CLIENT_LOGINSTATE))

local_player = me(client)
print(f"{local_player = }")

local_player2 = me(client)
print(f"{local_player2 = }")

name = local_player.name()
print(f"{name = }")

name2 = local_player2.name()
print(f"{name2 = }")