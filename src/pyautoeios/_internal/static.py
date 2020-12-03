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

import random
import sys
import time
from typing import Tuple

import pyautogui
from pyscreeze import Box

from pyautoeios._internal import hooks
from pyautoeios._internal.rs_actor import base_x, base_y
from pyautoeios._internal.rs_local_player import RSLocalPlayer
from pyautoeios.eios import EIOS

_STATES = {
    (0, 10 , False): "WELCOME_SCREEN",
    (0, 10 , True): "WELCOME_SCREEN",
    (0, 30 , False): "TIMEOUT1",
    (2, 10, True): "ENTER_USERNAME",
    (2, 10, False): "ENTER_USERNAME",
    (2, 20, False): "LOADING_PLEASE_WAIT",
    (2, 20, True): "LOADING",
    (2, 25 , False): "MOVING_REGIONS",
    (2, 25 , True): "BETWEEN_STATES",
    (2, 30 , False): "NORMAL",
    (2, 30 , True): "CLICK_TO_PLAY",
    (2, 45 , False): "SWITCHING_WORLD",
    (2, 45 , True): "SWITCHING_WORLD",
    (24, 10 , False): "DISCONNECTED",
    (24, 10 , True): "DISCONNECTED",
}

def game_state(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_GAMESTATE)

def _is_client_loading(eios: EIOS) -> bool:
    return eios.get_bool(None, hooks.CLIENT_ISLOADING)

def r_initialize_constants(eios: EIOS) -> None:
    raise NotImplementedError

def r_initialize_tile_settings(eios: EIOS) -> None:
    raise NotImplementedError

def r_initialize_tile_heights(eios: EIOS) -> None:
    raise NotImplementedError

def r_initialize_varp_masks(eios: EIOS) -> None:
    raise NotImplementedError

def is_client_loading(eios: EIOS) -> bool:
    _game_state = game_state(eios)
    return (
        (_game_state == 25)
        or (_game_state == 40)
        or (_game_state == 45)
        or _is_client_loading(eios)
    )

def update_region_cache(eios: EIOS) -> None:
    raise NotImplementedError

def loop_cycle(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_LOOPCYCLE)

def login_state(eios: EIOS) -> int:
    return eios.get_int(None, hooks.CLIENT_LOGINSTATE)

def get_client_dimensions(eios: EIOS) -> Tuple[int, int]:
    return eios.get_target_dimensions()

# def base_x(eios: EIOS) -> int:
#     return eios.get_int(None, hooks.CLIENT_BASEX)

# def base_y(eios: EIOS) -> int:
#     return eios.get_int(None, hooks.CLIENT_BASEY)

def shr(x: int, y: int) -> int:
    return x >> y

def shl(x: int, y: int) -> int:
    return x << y


def move_to_spot_in_box(box, **kwargs):
    # print(f"box = {box}")
    if "duration" not in kwargs:
        kwargs["duration"] = random.uniform(0.3, 1.1)
    if "tween" not in kwargs:
        kwargs["tween"] = pyautogui.easeOutQuad
    #
    cx, cy = pyautogui.center(box)
    x = random.randint(int(-1 * (box.width / 3)), int(box.width / 3)) + cx
    y = random.randint(int(-1 * (box.height / 3)), int(box.height / 3)) + cy
    # print(f"x = {x}, y = {y}")
    pyautogui.moveTo(x, y, **kwargs)


def click_on_spot_in_box(box, **kwargs):
    move_to_spot_in_box(box, **kwargs)
    pyautogui.click(**kwargs)


def click_disconnected(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 285
    left = (width // 2) - 67
    bottom = 317
    right = (width // 2) + 67
    box = Box(left, top, right - left, bottom - top)
    click_on_spot_in_box(box)


def click_existing_user(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 275
    left = (width // 2) + 12
    bottom = 307
    right = (width // 2) + 146
    box = Box(left, top, right - left, bottom - top)
    click_on_spot_in_box(box)


def click_email_prompt(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 245
    left = (width // 2) - 110
    bottom = 254
    right = (width // 2) - 73
    box = Box(left, top, right - left, bottom - top)
    click_on_spot_in_box(box)


def click_password_prompt(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 258
    left = (width // 2) - 108
    bottom = 267
    right = (width // 2) - 44
    box = Box(left, top, right - left, bottom - top)
    click_on_spot_in_box(box)


def click_login_button(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 305
    left = (width // 2) - 148
    bottom = 337
    right = (width // 2) - 14
    box = Box(left, top, right - left, bottom - top)
    click_on_spot_in_box(box)

def click_click_to_play(eios: EIOS):
    width, _ = get_client_dimensions(eios)
    top = 296
    left = (width // 2) - 110
    bottom = 378
    right = (width // 2) + 110
    box = Box(left, top, right - left, bottom - top)
    click_on_spot_in_box(box)


def count_pixels(box: Box) -> dict:
    """
    Returns a count of pixels per a unique color
    Args:
        box (BOX): the region of the screen to count all colors from
    Returns:
        a key-value pairing of the rgb color value and the number of times the color was present in the image
    """
    color_count = {}
    with pyautogui.screenshot(region=box) as image:
        width, height = image.size
        rgb_image = image.convert('RGB')
        # iterate through each pixel in the image and keep a count per unique color
        for x in range(width):
            for y in range(height):
                rgb = rgb_image.getpixel((x, y))
                if rgb in color_count:
                    color_count[rgb] += 1
                else:
                    color_count[rgb] = 1
    return color_count


def login(eios: EIOS, username:str, password: str) -> None:

    _state = get_complex_state(eios)
    if _state == "DISCONNECTED":
        click_disconnected(eios)
        time.sleep(0.5)
        while _state not in ("WELCOME_SCREEN", "ENTER_USERNAME"):
            _state = get_complex_state(eios)
            time.sleep(0.5)

    if _state == "WELCOME_SCREEN":
        click_existing_user(eios)
        time.sleep(0.5)
        while _state != "ENTER_USERNAME":
            _state = get_complex_state(eios)
            time.sleep(.5)

    if _state == "ENTER_USERNAME":

        # enter username if not present
        user_entered = eios.get_string(None, hooks.LOGIN_USERNAME)
        if user_entered != username:
            click_email_prompt(eios)
            eios.send_string("\b" * len(user_entered), 35, 10)
            eios.send_string(username, 100,100)

        # enter password if not present
        pass_entered = eios.get_string(None, hooks.LOGIN_PASSWORD)
        if pass_entered != password:
            click_password_prompt(eios)
            eios.send_string("\b" * len(pass_entered), 35, 10)
            eios.send_string(password, 100,100)

        # click login then wait for lobby
        click_login_button(eios)

        # if delete_username or False
        while _state != "CLICK_TO_PLAY":
            _state = get_complex_state(eios)
            time.sleep(.5)
            response1 = eios.get_string(None, hooks.LOGIN_RESPONSE1)
            if 'has been updated!' in response1:
                response2 = eios.get_string(None, hooks.LOGIN_RESPONSE2)
                sys.exit(f"Reopen the client. {response1} {response2}")
            if 'need a members account' in response1:
                response2 = eios.get_string(None, hooks.LOGIN_RESPONSE2)
                sys.exit(f"{response1} Manually set to F2P to continue.")




    # wait for click to play splash screen
    if _state == "CLICK_TO_PLAY":
        click_login_button(eios)
        while _state != "NORMAL":
            _state = get_complex_state(eios)
            time.sleep(.5)


def get_complex_state(eios: EIOS):
    _login_state = login_state(eios)
    _game_state = game_state(eios)
    _loading = _is_client_loading(eios)
    _state = _STATES.get((_login_state, _game_state, _loading), None)
    if not _state:
        # print(f"{_login_state = }, {_game_state = }, {_loading = }")
        return "UNKNOWN_STATE"
    return _state


def me(eios: EIOS) -> RSLocalPlayer:
    return RSLocalPlayer(eios)



# i = 0
# prev_complex_state = None
# while 1 < 10000000:
#     i += 1
#     complex_state = get_complex_state(_client)
#     if complex_state != prev_complex_state:
#         print(f"{i = }, {complex_state = }")
#     prev_complex_state = complex_state
