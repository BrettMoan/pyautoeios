# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List, TypeVar

from pyscreeze import Box, Point

from pyautoeios import hooks
from pyautoeios import static

from pyautoeios.rs_structures import RSType, get_rs_int_array, get_rs_string_array




WidgetList = List["RSWidget"]
W = TypeVar("W", List[WidgetList], WidgetList)

class RSWidget(RSType):
    def name(self) -> str:
        raise NotImplementedError

    def text(self) -> str:
        raise NotImplementedError

    def id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_WIDGETID)

    def parent_id(self) -> int:
        return static.shr(self.id(), 16)

    def group_id(self) -> int:
        raise NotImplementedError

    def child_id(self) -> int:
        raise NotImplementedError

    def item_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_ITEMID)

    def inventory_ids(self) -> List[int]:
        raise NotImplementedError

    def stack_sizes(self) -> List[int]:
        raise NotImplementedError

    def item_amount(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_ITEMAMOUNT)

    def texture_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_TEXTUREID)

    def actions(self) -> List[str]:
        raise NotImplementedError

    def action_type(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_ACTIONTYPE)

    def type_id(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_TYPE)

    def is_hidden(self) -> bool:
        raise NotImplementedError

    def cycle(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_WIDGETCYCLE)

    def absolute_x(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_ABSOLUTEX)

    def absolute_y(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_ABSOLUTEY)

    def relative_x(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_RELATIVEX)

    def relative_y(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_RELATIVEY)

    def scroll_x(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_SCROLLX)

    def scroll_y(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_SCROLLY)

    def width(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_WIDTH)

    def height(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_HEIGHT)

    def parent(self) -> RSWidget:
        raise NotImplementedError

    def child(self, index: int) -> RSWidget:
        raise NotImplementedError

    def children(self) -> List[RSWidget]:
        raise NotImplementedError

    def bounds_index(self) -> int:
        return self.eios._Reflect_Int(self.ref, hooks.WIDGET_BOUNDSINDEX)

    def bounds_x(self) -> int:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.CLIENT_WIDGETPOSITIONX,
            max_size=self.bounds_index()
        )

    def bounds_y(self) -> int:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.CLIENT_WIDGETPOSITIONY,
            max_size=self.bounds_index()
        )

    def absolute_location(self) -> Point:
        raise NotImplementedError

    def bounds(self) -> Box:
        raise NotImplementedError

    def get(self, container_index: int, parent: int, child: int = -1) -> RSWidget:
        raise NotImplementedError

    def get_parent(self, parent_id: int) -> RSWidget:
        raise NotImplementedError

    def root_interface(self) -> int:
        raise NotImplementedError

    def valid_interfaces(self) -> List[bool]:
        raise NotImplementedError

    def is_valid(self, group: int, child: int, index: int = -1) -> bool:
        raise NotImplementedError

    def widgets(self, index: int = None) -> W:
        raise NotImplementedError
