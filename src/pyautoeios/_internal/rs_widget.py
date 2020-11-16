#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.

# annotations allows methods of a class to return an object of that class
# i.e in in RSTile to annotate a return type of RSTile.
# see this thread: https://stackoverflow.com/a/33533514/4188287
from __future__ import annotations
from typing import List, TypeVar

from pyscreeze import Box, Point

from pyautoeios._internal import hooks
from pyautoeios._internal import static
from pyautoeios._internal.constants import RWidget
from pyautoeios.eios import (
    # EIOS,
    # SIZE,
    # CHAR,
    # BYTE,
    # BOOL,
    # SHORT,
    # INT,
    # LONG,
    # FLOAT,
    # DOUBLE,
    # STRING,
    OBJECT,
)


from pyautoeios._internal.rs_structures import RSType, get_rs_int_array, get_rs_string_array, get_rs_object_array


WidgetList = List["RSWidget"]
W = TypeVar("W", List[WidgetList], WidgetList)


class RSWidget(RSType):
    def name(self) -> str:
        raise NotImplementedError

    def text(self) -> str:
        raise NotImplementedError

    def id(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_WIDGETID)

    def parent_id(self) -> int:
        raise NotImplementedError

    def group_id(self) -> int:
        return static.shr(self.id(), 16)

    def child_id(self) -> int:
        return self.id() & 0xFFFF

    def item_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_ITEMID)

    def inventory_ids(self) -> List[int]:
        raise NotImplementedError

    def stack_sizes(self) -> List[int]:
        raise NotImplementedError

    def item_amount(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_ITEMAMOUNT)

    def texture_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_TEXTUREID)

    def actions(self) -> List[str]:
        raise NotImplementedError

    def action_type(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_ACTIONTYPE)

    def type_id(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_TYPE)

    def is_hidden(self) -> bool:
        if self.eios.get_bool(self.ref, hooks.WIDGET_ISHIDDEN):
            return True
        parent = self.parent()
        if parent:
            return parent.is_hidden()

        return self.group_id() != self.root_interface()

    def cycle(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_WIDGETCYCLE)

    def absolute_x(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_ABSOLUTEX)

    def absolute_y(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_ABSOLUTEY)

    def relative_x(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_RELATIVEX)

    def relative_y(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_RELATIVEY)

    def scroll_x(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_SCROLLX)

    def scroll_y(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_SCROLLY)

    def width(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_WIDTH)

    def height(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_HEIGHT)

    def parent(self) -> RSWidget:
        raise NotImplementedError

    def child(self, index: int = -1) -> RSWidget:
        if index == -1:
            raise ValueError
        _ref, _size = self.eios.get_array_with_size(self.ref, hooks.WIDGET_CHILDREN)
        if not _ref:
            return None
        if not _size or index >= _size:
            self.eios.release_object(_ref)
            return None
        widget_ref = self.eios.get_array_from_pointer(_ref, OBJECT, index)
        widget = RSWidget(self.eios, widget_ref)
        return widget

    def children(self) -> List[RSWidget]:
        raise NotImplementedError

    def bounds_index(self) -> int:
        return self.eios.get_int(self.ref, hooks.WIDGET_BOUNDSINDEX)

    def bounds_x(self) -> int:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.CLIENT_WIDGETPOSITIONX,
            max_size=self.bounds_index(),
        )

    def bounds_y(self) -> int:
        return get_rs_int_array(
            eios=self.eios,
            ref=None,
            hook=hooks.CLIENT_WIDGETPOSITIONY,
            max_size=self.bounds_index(),
        )

    def absolute_location(self) -> Point:
        raise NotImplementedError

    def bounds(self) -> Box:
        raise NotImplementedError

    def get(self, container_index: int, parent: int, child: int = -1) -> RSWidget:
        _ref = self.eios.get_array(None, hooks.CLIENT_WIDGETS)
        print(f"{_ref = }")
        if not _ref:
            return None

        widget_ref = self.eios.get_2d_array_index_from_pointer(
                instance=_ref,
                arr_type=OBJECT,
                x=container_index,
                y=parent,
            )
        print(f"{widget_ref = }")

        widget = RSWidget(self.eios, widget_ref)
        print(f"{widget = }")

        if child == -1:
            self.eios.release_object(_ref)
            return widget

        print(f"{child = }")
        child_widget = widget.child(child)

        print(f"{child_widget = }")

        self.eios.release_object(_ref)
        return child_widget

    def get_parent(self, parent_id: int) -> RSWidget:
        raise NotImplementedError

    def root_interface(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_WIDGETROOTINTERFACE)

    def valid_interfaces(self) -> List[bool]:
        raise NotImplementedError

    @classmethod
    def is_valid(cls, group: int, child: int, index: int = -1) -> bool:
        widget = cls.get(group,child,index)
        return widget is not None and not widget.is_hidden()

    def widgets(self, index: int = None) -> W:
        raise NotImplementedError
