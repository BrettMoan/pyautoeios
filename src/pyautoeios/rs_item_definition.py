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

# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List

from pyautoeios import hooks
from pyautoeios.rs_cache import RSCache
from pyautoeios.rs_structures import RSType, get_rs_string_array


class RSItemDefinition(RSType):
    def id(self) -> int:
        return self.eios.get_int(self.ref, hooks.ITEMDEFINITION_ID)

    def name(self) -> str:
        return self.eios.get_string(self.ref, hooks.ITEMDEFINITION_NAME)

    def is_members(self) -> bool:
        return self.eios.get_bool(self.ref, hooks.ITEMDEFINITION_ISMEMBERS)

    def actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMDEFINITION_ACTIONS,
        )

    def ground_actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=self.ref,
            hook=hooks.ITEMDEFINITION_GROUNDACTIONS,
        )

    def definition_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.ITEMDEFINITION_CACHE)
        return RSCache(self.eios, _ref)

    def get(self, id: int) -> RSItemDefinition:
        raise NotImplementedError
