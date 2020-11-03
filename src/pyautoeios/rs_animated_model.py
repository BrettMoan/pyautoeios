from pyautoeios import hooks
from pyautoeios.rs_structures import RSType


class RSAnimatedModel(RSType):
    def triangle_faces(self):
        raise NotImplementedError

    def triangles(self):
        raise NotImplementedError

    def animate(self):
        raise NotImplementedError

    def transform(self):
        raise NotImplementedError
