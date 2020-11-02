from typing import List
from pyautoeios.eios import EIOS, ReflectionArrayType
from pyautoeios.rs_structures import RSType, RSIntArray, RSStringArray
from pyautoeios import hooks
from pyscreeze import Box, Point


class RSClient(RSType):

    def loop_cycle(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_LOOPCYCLE)

    def login_state(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_LOGINSTATE)

    def game_state(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_GAMESTATE)

    def plane(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_PLANE)

    def plane(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_PLANE)

    def base_x(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_BASEX)

    def base_y(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_BASEY)

    def destination_x(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_DESTINATIONX)

    def destination_y(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_DESTINATIONY)

    def view_port_width(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_VIEWPORTWIDTH)

    def view_port_height(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_VIEWPORTHEIGHT)

    def view_port_scale(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_VIEWPORTSCALE)

    def map_angle(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_MAPANGLE)

    def player_count(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_PLAYERCOUNT)

    def menu_count(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_MENUCOUNT)

    def menu_width(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_MENUWIDTH)

    def menu_height(self) -> int:
        return self.eios._Reflect_Int(None, hooks.CLIENT_MENUHEIGHT)

    def is_menu_open(self) -> bool:
        return self.eios._Reflect_Bool(None, hooks.CLIENT_ISMENUOPEN)

    def menu_location(self) -> Point:
        x  = self.eios._Reflect_Int(None, hooks.CLIENT_MENUX)
        y  = self.eios._Reflect_Int(None, hooks.CLIENT_MENUY)
        return Point(x, y)

    def menu_bounds(self) -> Box:
        point  = self.menu_location()
        width = self.menu_width()
        height = self.menu_height()
        return Box(point.x, point.y, width ,height)

    def menu_options(self) -> List[str]:
        _ref, size = self.eios._Reflect_Array_With_Size(None, hooks.CLIENT_MENUOPTIONS)
        if _ref and size:
            options = RSStringArray(self.eios, _ref, size)
            return options

    def menu_actions(self) -> List[str]:
        _ref, size = self.eios._Reflect_Array_With_Size(None, hooks.CLIENT_MENUACTIONS)
        if _ref and size:
            options = RSStringArray(self.eios, _ref, size)
            return options
