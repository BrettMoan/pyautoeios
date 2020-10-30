from ctypes import c_void_p
import weakref

from pyautoeios.eios import EIOS
from pyautoeios.rs_structures import RSType
from pyautoeios import hooks


class RSPlayer(RSType):
    def name(self):
        _ref = self.eios._Reflect_Object(self.ref, hooks.PLAYER_NAME)
        name_info = RSNameInfo(self.eios, _ref)
        name = name_info.name()
        return name

class RSNameInfo(RSType):
    def name(self):
        return self.eios._Reflect_String(self.ref, hooks.NAMEINFO_NAME)

def me(eios: EIOS):
    return RSPlayer(eios, eios._Reflect_Object(None, hooks.CLIENT_LOCALPLAYER))

