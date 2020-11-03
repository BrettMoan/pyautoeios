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
print(f"{len(menu_options) = }")
# print all the menu actions
joined_and_filtered = [
    " ".join(item).strip()
    for item in zip(menu_actions, menu_options)
    if item[0] or item[1]
]
print(f"{len(joined_and_filtered) = } ")
print(joined_and_filtered)
