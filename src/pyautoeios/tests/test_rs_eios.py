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

"""Test pyautoeios.eios module."""
import os

import pyautoeios as pyauto
from pyautoeios.hexcodes import VK_ESC, VK_LBUTTON

# pylint: disable=protected-access, missing-function-docstring

PLAYER_EMAIL = os.environ.get("PLAYER_EMAIL", None)

def test__get_client_pids():
    """
    Tests:
        - eios.EIOS._get_client_pids
    """
    data = pyauto.eios.EIOS._get_client_pids()
    assert isinstance(data, list) and len(data) == 1


def test_get_clients():
    """
    Tests:
        - eios.EIOS._get_client_pids
    """
    data = pyauto.eios.EIOS.get_clients()
    assert isinstance(data, list) and len(data) == 1



def test_get_client_pid(client):
    """
    Tests:
        - eios.EIOS.get_client_pid
    """
    pid = pyauto.eios.EIOS.get_client_pid(0)
    assert client._pid == pid


def test_pair_client(client):
    """
    Tests:
        - eios.EIOS._eios_pair_client
    """
    ref =  pyauto.eios.EIOS._eios_pair_client(client._pid)
    assert ref == client._eios_ptr



def test_get_eios(client):
    """
    Tests:
        - eios.EIOS.get_eios
    """
    ref = pyauto.eios.EIOS.get_eios(client._pid)
    assert client._eios_ptr == ref

def test_release_target(client):
    """
    Tests:
        - eios.EIOS.release_target
        - eios.EIOS._eios_inject_pid
        - eios.EIOS._eios_pair_client
    """
    ref = client._eios_ptr
    pid = client._pid
    client.release_target()
    pyauto.eios.EIOS._eios_inject_pid(pid)
    new_ref = pyauto.eios.EIOS._eios_pair_client(pid)
    pyauto.eios.EIOS._clients[pid] = new_ref
    assert ref != new_ref


def test_get_target_dimensions(client):
    """
    Tests:
        - eios.EIOS.get_target_dimensions
    """
    width, height = client.get_target_dimensions()
    assert isinstance(width, int) and isinstance(height, int)


def test_get_string(client):
    """
    Tests:
        - eios.EIOS.get_string
    """
    got = client.get_string(None, pyauto.hooks.LOGIN_USERNAME)
    assert got == PLAYER_EMAIL


def test_has_focus(client):
    """
    Tests:
        - eios.EIOS.has_focus
    """
    assert isinstance(client.has_focus(), bool)


def test_lose_focus(client):
    """
    Tests:
        - eios.EIOS.lose_focus
        - eios.EIOS.has_focus
    """
    client.lose_focus()
    assert not client.has_focus()


def test_gain_focus(client):
    """
    Tests:
        - eios.EIOS.gain_focus
        - eios.EIOS.has_focus
    """
    client.gain_focus()
    assert client.has_focus()


def test_is_key_held(client):
    """
    Tests:
        - eios.EIOS.is_key_held
    """
    assert isinstance(client.is_key_held(VK_ESC), bool)


def test_hold_key(client):
    """
    Tests:
        - eios.EIOS.hold_key
    """
    client.hold_key(VK_ESC)
    assert client.is_key_held(VK_ESC)


def test_release_key(client):
    """
    Tests:
        - eios.EIOS.release_key
    """
    client.release_key(VK_ESC)
    assert not client.is_key_held(VK_ESC)


def test_something():
    pass
