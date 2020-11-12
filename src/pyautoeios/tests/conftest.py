
import os
from getpass import getpass

import pytest

import pyautoeios as pyauto

EIOS = pyauto.eios.EIOS

# pylint: disable=protected-access
# pylint: disable=redefined-outer-name

PLAYER_EMAIL = os.environ.get("PLAYER_EMAIL", None)
if not PLAYER_EMAIL:
    os.environ["PLAYER_EMAIL"] = PLAYER_EMAIL = input(prompt="Enter user email:")

PLAYER_NAME = os.environ.get("PLAYER_NAME", None)
if not PLAYER_NAME:
    os.environ["PLAYER_NAME"] = PLAYER_NAME = input(prompt="Enter expected username:")

PLAYER_PASSWORD = os.environ.get("PLAYER_PASSWORD", None)
if not PLAYER_PASSWORD:
    os.environ["PLAYER_PASSWORD"] = PLAYER_PASSWORD = getpass(prompt="Enter password:")

PLAYER_STATS = os.environ.get("PLAYER_STATS", None)
if not PLAYER_STATS:
    os.environ["PLAYER_STATS"] = PLAYER_STATS = getpass(prompt="Enter player stats (in fmt [N,N,...N,N]):")


@pytest.fixture(scope="session")
def client() -> EIOS:
    """
    Tests:
        - eios.EIOS.__init__
        - eios.EIOS._get_client_pids
        - eios.EIOS._eios_inject_pid
        - eios.EIOS._eios_pair_client

    """
    _client = pyauto.eios.EIOS()
    assert (
        isinstance(_client, pyauto.eios.EIOS)
        and isinstance(_client._pid, int)
        and isinstance(_client._eios_ptr, int)
    )
    pyauto.pair_client(_client)
    pyauto.static.login(_client, PLAYER_EMAIL, PLAYER_PASSWORD)
    yield _client
    pid = _client._pid
    _client._cleanup()
    assert not pyauto.eios.EIOS._objects.get(pid) and pid not in pyauto.eios.EIOS._clients.keys()






# import importlib
# pyauto = importlib.reload(pyauto)
# import pyautoeios as pyauto
# from pyautoeios import pyauto
# from pyautoeios.eios import EIOS
# _client = EIOS()
# pyauto.pair_client(_client)
# pyauto.click_existing_user(_client)

# pyauto.click_login_button(_client)
