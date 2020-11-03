import ctypes
import pyautoeios as pyauto
from pyautoeios import hooks

from pyautoeios.rs_player import me
from pyautoeios.rs_client import RSClient
from pyautoeios.rs_structures import RSObjectArray
from pyautoeios.rs_npc import RSNPC


pyauto.inject_clients()
client = pyauto.clients[0]
pyauto.pair_client(client)

rs_client = RSClient(client, None)
# indices = rs_client.npc_indices()
# shrunk = [i for i in indices if i]
# print(shrunk)

# client._Reflect_Array_Indices()
# npcs_ref, npcs_size = client._Reflect_Array_With_Size(None, hooks.CLIENT_LOCALNPCS)
# print(f"{npcs_ref = }, {npcs_size = }")

# npcs = RSObjectArray(client, npcs_ref, npcs_size, indices=shrunk)
# print(f"{npcs = }, {npcs._elements = }")

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
