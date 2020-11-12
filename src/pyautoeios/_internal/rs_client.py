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

from typing import List

from pyscreeze import Box, Point

from pyautoeios import hooks
from pyautoeios import static
from pyautoeios.eios import EIOS
from pyautoeios._internal.rs_npc import RSNPC
from pyautoeios._internal.rs_cache import RSCache
from pyautoeios._internal.rs_player import RSPlayer
from pyautoeios._internal.rs_region import RSRegion
from pyautoeios._internal.rs_structures import (
    RSType,
    RSObjectArray,
    get_rs_int_array,
    get_rs_string_array,
)


class RSClient(RSType):
    def loop_cycle(self) -> int:
        return static.loop_cycle(self.eios)

    def login_state(self) -> int:
        return static.login_state(self.eios)

    def game_state(self) -> int:
        return static.game_state(self.eios)

    def is_loading(self) -> bool:
        return static.is_client_loading(self.eios)

    def get_tile_settings(self, x: int, y: int, z: int) -> int:
        raise NotImplementedError

    def get_tile_heights(self, x: int, y: int, z: int) -> int:
        raise NotImplementedError

    def plane(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_PLANE)

    def base_x(self) -> int:
        return static.base_x(self.eios)

    def base_y(self) -> int:
        return static.base_y(self.eios)

    def destination_x(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_DESTINATIONX)

    def destination_y(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_DESTINATIONY)

    def view_port_width(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_VIEWPORTWIDTH)

    def view_port_height(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_VIEWPORTHEIGHT)

    def view_port_scale(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_VIEWPORTSCALE)

    def map_angle(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_MAPANGLE)

    def npc_indices(self, npc_count: int = None) -> List[int]:
        return get_rs_int_array(
            self.eios, ref=None, hook=hooks.CLIENT_NPCINDICES, max_size=npc_count
        )

    def npc_count(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_NPCCOUNT)

    def player_indices(self, player_count: int = None) -> List[int]:
        return get_rs_int_array(
            self.eios, ref=None, hook=hooks.CLIENT_PLAYERINDICES, max_size=player_count
        )

    def player_count(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_PLAYERCOUNT)

    def all_npcs(self):
        npcs_ref, npcs_size = self.eios.get_array_with_size(
            None, hooks.CLIENT_LOCALNPCS
        )
        print(f"{npcs_ref = }, {npcs_size = }")
        if npcs_ref:
            indices = self.npc_indices()
            shrunk = [i for i in indices if i]
            npcs = RSObjectArray(self.eios, npcs_ref, npcs_size, indices=shrunk)
            return [RSNPC(self.eios, npc_ref) for npc_ref in npcs.elements if npc_ref]
        return None

    def all_players(self) -> List[RSPlayer]:
        players_ref, players_size = self.eios.get_array_with_size(
            None, hooks.CLIENT_LOCALPLAYERS
        )
        if players_ref:
            indices = self.player_indices()
            shrunk = [i for i in indices if i]
            players = RSObjectArray(
                self.eios, players_ref, players_size, indices=shrunk
            )
            return [
                RSPlayer(self.eios, npc_ref)
                for npc_ref in players.elements[:]
                if npc_ref
            ]
        return None

    def animation_frame_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.CLIENT_ANIMATIONFRAMECACHE)
        return RSCache(self.eios, _ref)

    def item_node_cache(self) -> RSCache:
        _ref = self.eios.get_object(None, hooks.CLIENT_ITEMNODECACHE)
        return RSCache(self.eios, _ref)

    def region(self) -> RSRegion:
        _ref = self.eios.get_object(None, hooks.CLIENT_REGION)
        return RSRegion(self.eios, _ref)

    def is_region_instanced(self) -> bool:
        return self.eios.get_bool(None, hooks.CLIENT_ISREGIONINSTANCED)

    def region_instance_chunk(self, plane: int, chunk_x: int, chunk_y: int) -> int:
        raise NotImplementedError

    def region_instance_chunks(self, plane: int) -> List[List[int]]:
        raise NotImplementedError

    def is_resizeable(self) -> bool:
        width, height = static.get_client_dimensions(self.eios)
        return width != 765 or height != 503

    def get_var_bit(self, id: int) -> int:
        raise NotImplementedError

    def menu_actions(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=None,
            hook=hooks.CLIENT_MENUACTIONS,
        )

    def menu_options(self) -> List[str]:
        return get_rs_string_array(
            eios=self.eios,
            ref=None,
            hook=hooks.CLIENT_MENUOPTIONS,
        )

    def menu_count(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_MENUCOUNT)

    def menu_location(self) -> Point:
        x = self.eios.get_int(None, hooks.CLIENT_MENUX)
        y = self.eios.get_int(None, hooks.CLIENT_MENUY)
        return Point(x, y)

    def menu_width(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_MENUWIDTH)

    def menu_height(self) -> int:
        return self.eios.get_int(None, hooks.CLIENT_MENUHEIGHT)

    def menu_bounds(self) -> Box:
        point = self.menu_location()
        width = self.menu_width()
        height = self.menu_height()
        return Box(point.x, point.y, width, height)

    def is_menu_open(self) -> bool:
        return self.eios.get_bool(None, hooks.CLIENT_ISMENUOPEN)
