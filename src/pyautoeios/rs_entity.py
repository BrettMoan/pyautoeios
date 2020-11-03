from pyautoeios import hooks
from pyautoeios.rs_structures import RSType


class RSEntity(RSType):
    def model_height(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.RENDERABLE_MODELHEIGHT)
