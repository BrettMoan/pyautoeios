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


import pyautoeios as pyauto
from pyautoeios.rs_client import RSClient
from pyautoeios import hooks
from pyautoeios.rs_structures import RSObjectArray
from pyautoeios.rs_npc import RSNPC

import pyautoeios as pyauto
from pyautoeios.rs_player import me

pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)
rs_client = RSClient(client, None)
# indices = rs_client.npc_indices()
# shrunk = [i for i in indices if i]
# print(shrunk)
# npcs_ref, npcs_size = client.get_array_with_size(None, hooks.CLIENT_LOCALNPCS)
# print(f"{npcs_ref = }, {npcs_size = }")
# npcs = RSObjectArray(client, npcs_ref, npcs_size, indices=shrunk)
# print(f"{npcs = }, {npcs.elements = }")
# client.get_array_indices()
# result_type = ctypes.c_void_p * len(shrunk)
# foo = ctypes.cast(npcs._elements, ctypes.POINTER(result_type))
# print(f"{foo = } {foo.contents = } {foo.contents[:] = }")
# npc_array = []
# for i in foo.contents[:]:
#     if i:
#         print(f"{i = }")
#         npc = RSNPC(client, i)
#         print(f"{npc = }")
#         definition = npc.definition()
#         print(f"{definition = }")
#         if definition:
#             npc_array.append({
#                 "name": definition.name(),
#                 "id" : definition.id(),
#             })
npcs = rs_client.all_npcs()
# npc = npcs[0]
# definition = npc.definition()
npc_array = []
for npc in rs_client.all_npcs():
    definition = npc.definition()
    if definition:
        npc_array.append(
            {
                "name": definition.name(),
                "id": definition.id(),
            }
        )

print(npc_array)
