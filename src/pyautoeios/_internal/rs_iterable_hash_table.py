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

from pyautoeios._internal import hooks
from pyautoeios._internal.rs_node import RSNode
from pyautoeios._internal.rs_structures import RSType


class RSIterableHashTable(RSType):
    def head(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.ITERABLEHASHTABLE_HEAD)
        return RSNode(self.eios, _ref)

    def tail(self) -> RSNode:
        _ref = self.eios.get_object(self.ref, hooks.ITERABLEHASHTABLE_TAIL)
        return RSNode(self.eios, _ref)

    def bucket(self, Index: int) -> RSNode:
        raise NotImplementedError
        # Buckets: Pointer;
        # BucketsSize: int;
        # Buckets := RGetArray(R_EIOS, ref, BucketsSize, ITERABLEHASHTABLE_BUCKETS);
        # if Buckets = nil then
        #     Exit;

        # Result.ref := RGetObjectArray(R_EIOS, Buckets, Index);
        # RFreeObject(R_EIOS, Buckets);

    def buckets(self) -> List[RSNode]:
        raise NotImplementedError
        # Buckets: Pointer;
        # Nodes: Array of Pointer;
        # I, BucketsSize: int;
        # BucketsSize := 0;
        # Buckets := RGetArray(R_EIOS, ref, BucketsSize, ITERABLEHASHTABLE_BUCKETS);
        # if Buckets = nil then
        #     Exit;

        # Nodes := RGetObjectArray(R_EIOS, Buckets, 0, BucketsSize);
        # RFreeObject(R_EIOS, Buckets);

        # SetLength(Result, BucketsSize);

        # for I := 0 to BucketsSize - 1 do

        #     Result[I].ref := Nodes[I];

    def index(self) -> int:
        return self.eios.get_int(self.ref, hooks.ITERABLEHASHTABLE_INDEX)

    def size(self) -> int:
        return self.eios.get_int(self.ref, hooks.ITERABLEHASHTABLE_SIZE)

    def get_object(self, ID: int) -> RSNode:
        raise NotImplementedError
        # Index, HeadUID, CurrentUID: int;
        # Head, Current: RSNode;
        # Result.ref := nil;
        # Index := ID and (self.Size - 1);
        # Head := self.Bucket(Index);

        # if Head.ref <> nil then
        #     Current := Head.Next;
        #     if Current.ref <> nil then

        #         while HeadUID <> (CurrentUID := Current.UID) do
        #             if CurrentUID = ID then
        #                 Exit(Current);

        #             if CurrentUID = -1 then
        #                 break;

        #             Current := Current.Next;
