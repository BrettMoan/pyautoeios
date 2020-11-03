from pyscreeze import Point

from pyautoeios import hooks
from pyautoeios import static
from pyautoeios.rs_structures import RSType


class RSActor(RSType):
    def spoken_text(self) -> str:
        return self.eios._Reflect_String(self.ref, hooks.ACTOR_SPOKENTEXT)

    def orientation(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_ORIENTATION)

    def local_x(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_LOCALX)

    def local_y(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_LOCALY)

    def local_tile(self) -> Point:
        return Point(self.local_x(), self.local_y())

    def tile(self) -> Point:
        x = static.base_x(self.eios) + self.local_x() % 128
        y = static.base_y(self.eios) + self.local_y() % 128
        return Point(x, y)

    def animation_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_ANIMATION)

    def is_animating(self) -> bool:
        return self.animation_id() > -1

    def spot_animation(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_SPOTANIMATION)

    def spot_animation_frame(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_SPOTANIMATIONFRAME)

    def spot_animation_frame_cycle(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_SPOTANIMATIONFRAMECYCLE)

    def graphics_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_GRAPHICSID)

    def animation_frame(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_ANIMATIONFRAME)

    def movement_sequence_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_MOVEMENTSEQUENCE)

    def movement_frame(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_MOVEMENTFRAME)

    def current_sequence_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_CURRENTSEQUENCE)

    def is_idle(self) -> bool:
        return not self.is_animating()

    def interacting_index(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.ACTOR_INTERACTINGINDEX)

    def health(self) -> int:
        raise NotImplementedError

    def health_ratio(self) -> int:
        raise NotImplementedError

    def health_scale(self) -> int:
        raise NotImplementedError

    def health_percentage(self):
        raise NotImplementedError

    def is_in_combat(self):
        raise NotImplementedError

    def get_interacting(self):
        raise NotImplementedError

    def in_box(self):
        raise NotImplementedError
