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

# import ctypes
from pyautoeios._internal import hooks

import pyautoeios as pyauto
from pyautoeios._internal.rs_model import RSModel



# from pyautoeios.eios import (
#     EIOS, OBJECT,
#     # SIZE, CHAR, BYTE, BOOL, SHORT, INT, LONG, FLOAT, DOUBLE, STRING,
# )

pyauto.inject_clients()
with pyauto.clients.pop(0) as client:
    pyauto.pair_client(client)
    local_player = pyauto.static.me(client)
    definition = local_player.definition()
    # Cache = definition.model_cache()
    # HashTable = Cache.hash_table()
    # ModelID = definition.animated_model_id()
    # model.ref = HashTable.GetObject(ModelID).ref
    # print("local_player = ", local_player)
    # print("definition = ", definition)
    # print("Cache = ", Cache)
    # print("HashTable = ", HashTable)
    # print("ModelID = ", ModelID)
    # node = HashTable.get_object(ModelID)
    # print("node = ", node)
    # model = RSModel(node.eios, node.ref)
    # print("model = ", model)
    print(f"{definition.cached_model().raw_vertices() = }")
