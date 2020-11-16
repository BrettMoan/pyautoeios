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

import pyautoeios as pyauto

from pyautoeios._internal import constants
from pyautoeios._internal import hooks
from pyautoeios._internal import static

from pyautoeios.eios import OBJECT
from pyautoeios._internal.rs_widget import RSWidget

client = pyauto.eios.EIOS()


_ref = client.get_array(None, hooks.CLIENT_WIDGETS)
print(f"{_ref = }")

# client.release_object(_ref)

container_index = constants.R_BANK_INVENTORY_ITEM_CONTAINER.group
parent = constants.R_BANK_INVENTORY_ITEM_CONTAINER.child

widget_ref = client.get_2d_array_index_from_pointer(
                instance=_ref,
                arr_type=OBJECT,
                x=container_index,
                y=parent,
            )
print(f"{widget_ref = }")

wid = client.get_int(widget_ref, hooks.WIDGET_WIDGETID)
print(f"{wid = }")

widget = RSWidget(client, widget_ref)
print(f"{widget = }")

# print(f"{widget.name() = }")
# print(f"{widget.text() = }")
print(f"{widget.id() = }")
# print(f"{widget.parent_id() = }")
print(f"{widget.group_id() = }")
print(f"{widget.child_id() = }")
print(f"{widget.item_id() = }")
# print(f"{widget.inventory_ids() = }")
# print(f"{widget.stack_sizes() = }")
print(f"{widget.item_amount() = }")
print(f"{widget.texture_id() = }")
# print(f"{widget.actions() = }")
print(f"{widget.action_type() = }")
print(f"{widget.type_id() = }")
# print(f"{widget.is_hidden() = }")
print(f"{widget.cycle() = }")
print(f"{widget.absolute_x() = }")
print(f"{widget.absolute_y() = }")
print(f"{widget.relative_x() = }")
print(f"{widget.relative_y() = }")
print(f"{widget.scroll_x() = }")
print(f"{widget.scroll_y() = }")
print(f"{widget.width() = }")
print(f"{widget.height() = }")
# print(f"{widget.parent() = }")
# print(f"{widget.child() = }")
# print(f"{widget.children() = }")
print(f"{widget.bounds_index() = }")
print(f"{widget.bounds_x() = }")
print(f"{widget.bounds_y() = }")
# print(f"{widget.absolute_location() = }")
# print(f"{widget.bounds() = }")
print(f"{widget.get(container_index, parent) = }")
# print(f"{widget.get_parent() = }")
print(f"{widget.root_interface() = }")
# print(f"{widget.valid_interfaces() = }")
# print(f"{widget.is_valid() = }")
# print(f"{widget.widgets() = }")


# client.release_object(widget_ref)
####### FROM SIMBA
# ret_val.Name=
# ret_val.Text=
# ret_val.Id=983043
# ret_val.ParentID=983041
# ret_val.GroupID=15
# ret_val.ChildID=3
# ret_val.ItemID=-1
# ret_val.IsHidden=False
#######


# var
#   Widgets: Pointer;
#   wParent: RSWidget;
#   ret_val: RSWidget;
#   ContainerIndex, Parent, Child: Int32;
# begin
#   ClearDebug;
#   ContainerIndex := R_BANK_INVENTORY_ITEM_CONTAINER.Group;
#   Parent := R_BANK_INVENTORY_ITEM_CONTAINER.Child;
#   Widgets := RGetArray(R_EIOS, nil, CLIENT_WIDGETS);
#   writeln(Widgets);
#   ret_val.ref := RGetObjectArray2D(R_EIOS, Widgets, ContainerIndex, Parent);
#   writeln(ret_val);
#   writeln("ret_val.Name=", ret_val.Name);
#   writeln("ret_val.Text=", ret_val.Text);
#   writeln("ret_val.Id=", ret_val.Id);
#   writeln("ret_val.ParentID=", ret_val.ParentID);
#   writeln("ret_val.GroupID=", ret_val.GroupID);
#   writeln("ret_val.ChildID=", ret_val.ChildID);
#   writeln("ret_val.ItemID=", ret_val.ItemID);
#   writeln("ret_val.IsHidden=", ret_val.IsHidden);
#   RFreeObject(R_EIOS, Widgets);
#   ret_val.Free;
# end.
