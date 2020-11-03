from pyautoeios.rs_structures import RSType
from pyautoeios import hooks

from pyautoeios.rs_tile import RSTile
from pyautoeios.rs_client import RSClient
from pyautoeios.rs_animation_sequence import RSAnimationSequence


class RSAnimableNode(RSType):
    def id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_ID)

    def animation_sequence(self) -> RSAnimationSequence:
        _ref = self.eios._Reflect_Object(self.ref, hooks.ANIMABLENODE_ANIMATIONSEQUENCE)
        return RSAnimationSequence(self.eios, _ref)

    def animation_frame_id(self) -> int:
        return self.id()

    def flags(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_FLAGS)

    def orientation(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_ORIENTATION)

    def plane(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_PLANE)

    def local_x(self) -> int:
        x = self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_X)
        return (x << 7) + (1 << 6)

    def local_y(self) -> int:
        y = self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_Y)
        return (y << 7) + (1 << 6)

    def local_tile(self) -> RSTile:
        x = self.local_x()
        y = self.local_y()
        return RSTile(self.eios, x, y)

    def tile(self) -> RSTile:
        client = RSClient(self.eios, None)
        x = client.base_x() + self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_X)
        y = client.base_y() + self.eios._Reflect_Int(self.ref, hooks.ANIMABLENODE_Y)
        return RSTile(self.eios, x, y)
