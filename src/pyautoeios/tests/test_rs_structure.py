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
import json
import os

from pyautoeios._internal import hooks
from pyautoeios._internal import rs_structures

# pylint: disable=protected-access

PLAYER_STATS = json.loads(os.environ.get("PLAYER_STATS", None))

def test_rs_int_array(client):
    """
    tests:
        - pyautoeios.eios.EIOS.get_array
        - pyautoeios._internal.rs_structures.RSIntArray
    """
    _ref = client.get_array(None, hooks.CLIENT_CURRENTLEVELS)
    skills_array = rs_structures.RSIntArray(client, _ref)
    assert PLAYER_STATS == skills_array.all()

def test_get_npcs_at_grand_exchanges(client):
    """
    tests:
        - pyautoeios._internal.rs_structures.get_rs_int_array
        - pyautoeios._internal.rs_structures.RSObjectArray
        - pyautoeios._internal.rs_structures.RSType
        - pyautoeios.eios.EIOS.get_object
        - pyautoeios.eios.EIOS.get_string
        - pyautoeios.eios.EIOS.get_int
    """
    indices = rs_structures.get_rs_int_array(
        client, ref=None, hook=hooks.CLIENT_NPCINDICES, max_size=None
    )
    shrunk = [i for i in indices if i]
    npcs_ref, npcs_size = client.get_array_with_size(None, hooks.CLIENT_LOCALNPCS)
    print(f"{npcs_ref = }, {npcs_size = }")

    npcs_arr = rs_structures.RSObjectArray(
        client, npcs_ref, npcs_size, indices=shrunk
    )
    print(f"{npcs_arr = }, {npcs_arr.elements = }")

    npcs = [
        rs_structures.RSType(client, npc_ref)
        for npc_ref in npcs_arr.elements
        if npc_ref
    ]
    print(f"{npcs = }")

    npc_array = []
    for npc in npcs:
        _ref = client.get_object(npc.ref, hooks.NPC_DEFINITION)
        definition = rs_structures.RSType(client, _ref)
        if definition:
            _name = client.get_string(_ref, hooks.NPCDEFINITION_NAME)
            _id = client.get_int(_ref, hooks.NPCDEFINITION_ID)
            npc_array.append({"name": _name, "oid": _id})
    for i in npc_array:
        print(i)

    assert (
        len(npc_array) > 1
        and {"name": "Grand Exchange Clerk", "oid": 2149} in npc_array
        and {"name": "Grand Exchange Clerk", "oid": 2151} in npc_array
        and {"name": "Grand Exchange Clerk", "oid": 2148} in npc_array
        and {"name": "Grand Exchange Clerk", "oid": 2150} in npc_array
    )
