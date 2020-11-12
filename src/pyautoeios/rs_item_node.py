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

from typing import List
from pyautoeios import hooks
from pyautoeios.rs_hash_table import RSHashTable
from pyautoeios.rs_structures import RSType, get_rs_int_array


class RSItemNode(RSType):
    def item_ids(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMNODE_ITEMIDS,
        )

    def item_quantities(self) -> List[int]:
        return get_rs_int_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMNODE_ITEMQUANTITIES,
        )

    def hash_table(self) -> RSHashTable:
        _ref = self.eios.get_object(None, hooks.ITEMNODE_CACHE)
        return RSHashTable(self.eios, _ref)
