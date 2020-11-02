
from typing import List, Type

from pyscreeze import Point

from pyautoeios import hooks
from pyautoeios.rs_actor import RSActor
from pyautoeios.rs_model import RSModel
from pyautoeios.rs_npc_definition import RSNPCDefinition
from pyautoeios.rs_animated_model import RSAnimatedModel


T = Type['RSNPC']

class RSNPC(RSActor):
    def definition(self) -> RSNPCDefinition:
        _ref = self.eios._Reflect_Object(self.ref, hooks.NPC_DEFINITION)
        return RSNPCDefinition(self.eios, _ref)

    def all_npcs(self):
        raise NotImplementedError("moved to RSClient in python verison, to prevent circular imports")
        
    def model(self) -> RSModel:
        raise NotImplementedError

    def animated_model(self) -> RSAnimatedModel:
        raise NotImplementedError

    def to_tpa(self) -> List[Point]:
        raise NotImplementedError




    # Function RSNPC.Definition: RSNPCDefinition; constref;
    # Function RSNPC.AllNPCs: Array of RSNPC; static;
    # Function RSNPC.Model: RSModel; constref;
    # Function RSNPC.AnimatedModel: RSAnimatedModel; constref;
    # function RSNPC.ToTPA(): TPointArray
