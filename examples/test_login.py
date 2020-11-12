import os
from getpass import getpass

import pyautoeios as pyauto

_client = pyauto.eios.EIOS()
pyauto.pair_client(_client)

PLAYER_EMAIL = os.environ.get("PLAYER_EMAIL", None)
if not PLAYER_EMAIL:
    PLAYER_EMAIL = input("enter user email:")

PLAYER_PASSWORD = os.environ.get("PLAYER_PASSWORD", None)
if not PLAYER_PASSWORD:
    PLAYER_PASSWORD = getpass(prompt="enter password:")

pyauto.static.login(_client, PLAYER_EMAIL, PLAYER_PASSWORD)
