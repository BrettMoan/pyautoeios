from typing import Tuple
from pyautoeios.eios import EIOS
from pyautoeios import hooks

def is_client_loading(eios:EIOS) -> bool:
    game_state = eios._Reflect_Int(None, hooks.CLIENT_GAMESTATE);
    return (game_state == 25) or (game_state == 40) or (game_state == 45) or eios._Reflect_Bool(None, hooks.CLIENT_ISLOADING);

def get_client_dimensions(eios:EIOS) -> Tuple[int,int]:
    return eios._EIOS_GetTargetDimensions()

def base_x(eios:EIOS)
    return eios._Reflect_Int(None, hooks.CLIENT_BASEX)

def base_y(eios:EIOS)
    return eios._Reflect_Int(None, hooks.CLIENT_BASEY)
