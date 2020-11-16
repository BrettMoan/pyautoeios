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
"""Automation module designed to play old school."""
# pylint: disable=protected-access
# pylint: disable=wrong-import-order
# pylint: disable=ungrouped-imports
# pylint: disable=wrong-import-position

from typing import List
import random

from pyautoeios import eios
from pyautoeios import hexcodes
from pyautoeios._internal import static
from pyautoeios._internal import hooks
from pyautoeios._internal import _pyscreeze_remoteinput_patch
from pyautoeios._internal import _pyautogui_remoteinput_patch

import pyautogui as _gui

_gui.platformModule = _pyautogui_remoteinput_patch
_gui.screenshot = _pyscreeze_remoteinput_patch._screenshot_remoteinput
_gui.pyscreeze.screenshot = _pyscreeze_remoteinput_patch._screenshot_remoteinput


if _gui.pyscreeze.useOpenCV:
    from pyautoeios._internal import _pyscreeze_cv2_patch

    _gui.pyscreeze._load_cv2 = _pyscreeze_cv2_patch._load_cv2
    _gui.pyscreeze._extract_alpha_cv2 = _pyscreeze_cv2_patch._extract_alpha_cv2
    _gui.pyscreeze._locateAll_opencv = _pyscreeze_cv2_patch._locateAll_opencv

# Now that things have been patched, import all
# of pyautogui into the pyautoeios namespace
from pyautogui import *


clients = []


def inject_clients() -> List[eios.EIOS]:
    """Create all the EIOS clients."""
    try:
        while True:
            clients.append(eios.EIOS())
    except OSError:
        if len(clients) < 1:
            raise
    else:
        return clients


def pair_client(eios_obj: eios.EIOS):
    """Pair a client to use with pyautogui commands."""
    _pyautogui_remoteinput_patch.eios_obj = eios_obj
    _pyscreeze_remoteinput_patch.eios_obj = eios_obj



__AUTHOR__ = "brett.moan@gmail.com"
__VERSION__ = "0.0.7"
