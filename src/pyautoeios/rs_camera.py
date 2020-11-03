from pyautoeios import hooks
from pyautoeios.rs_structures import RSType


class RSCamera(RSType):
    def x(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_CAMERAX)

    def y(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_CAMERAY)

    def z(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_CAMERAZ)

    def pitch(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_CAMERAPITCH)

    def yaw(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_CAMERAYAW)
