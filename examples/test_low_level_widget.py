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

from pyautoeios import constants
from pyautoeios import hooks
from pyautoeios import static

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
client.get_int(widget_ref, hooks.WIDGET_WIDGETID)

widget = RSWidget(client, widget_ref)


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
