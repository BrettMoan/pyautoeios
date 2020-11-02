from typing import List

from pyautoeios import hooks
from pyautoeios.rs_node import RSNode
from pyautoeios.rs_structures import RSType

class RSIterableHashTable(RSType):
    def head(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.ITERABLEHASHTABLE_HEAD)
        return RSNode(self.eios, _ref)

    def tail(self) -> RSNode:
        _ref = self.eios._Reflect_Object(self.ref, hooks.ITERABLEHASHTABLE_TAIL)
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
        return self.eios._Reflect_Int(self.ref, hooks.ITERABLEHASHTABLE_INDEX)

    def size(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ITERABLEHASHTABLE_SIZE)

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
