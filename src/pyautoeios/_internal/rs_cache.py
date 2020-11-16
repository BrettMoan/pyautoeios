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

from pyautoeios._internal import hooks
from pyautoeios._internal.rs_iterable_hash_table import RSIterableHashTable
from pyautoeios._internal.rs_queue import RSQueue
from pyautoeios._internal.rs_structures import RSType


class RSCache(RSType):
    def hash_table(self) -> RSIterableHashTable:
        _ref = self.eios.get_object(self.ref, hooks.CACHE_HASHTABLE)
        return RSIterableHashTable(self.eios, _ref)

    def queue(self) -> RSQueue:
        _ref = self.eios.get_object(self.ref, hooks.CACHE_QUEUE)
        return RSQueue(self.eios, _ref)

    def remaining(self) -> int:
        return self.eios.get_int(self.ref, hooks.CACHE_REMAINING)

    def capacity(self) -> int:
        return self.eios.get_int(self.ref, hooks.CACHE_CAPACITY)
