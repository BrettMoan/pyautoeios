import ctypes
import pyautoeios as pyauto
from pyautoeios import hooks
from pyautoeios.rs_client import RSClient

pyauto.inject_clients()

client = pyauto.clients[0]
print(f"{client = }")

rs_client = RSClient(client, None)

from pyautoeios.rs_client import RSClient
menu_options = rs_client.menu_options()
menu_actions = rs_client.menu_actions()
print(f"{menu_options.size = }")
# print all the menu actions
print(menu_actions.all())
print(menu_options.all())
# print([" ".join(item).strip() for item in zip(menu_actions.all(), menu_options.all()) if item[0] or item[1]])
