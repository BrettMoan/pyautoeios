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
from pyautoeios.eios import EIOS
from pyautoeios._internal.rs_client import RSClient

# pylint: disable=protected-access, missing-function-docstring


def test_get_npcs_at_grand_exchanges(client):
    """
    tests:
        - rs_client.RSClient.all_npcs
        - rs_npc_definition.RSNPCDefinition.name
        - rs_npc_definition.RSNPCDefinition.id
    """
    rs_client = RSClient(client, None)
    npcs = rs_client.all_npcs()
    npc_array = []
    for npc in npcs:
        definition = npc.definition()
        if definition:
            npc_array.append(
                {
                    "name": definition.name(),
                    "id": definition.id(),
                }
            )
    for i in npc_array:
        print(i)
    assert (
        len(npc_array) > 1
        and {"name": "Grand Exchange Clerk", "id": 2149} in npc_array
        and {"name": "Grand Exchange Clerk", "id": 2151} in npc_array
        and {"name": "Grand Exchange Clerk", "id": 2148} in npc_array
        and {"name": "Grand Exchange Clerk", "id": 2150} in npc_array
    )
