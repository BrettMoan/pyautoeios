""" This module integrates remoteinput's EIOS methods with pyautogui.

EIOS implementation to interact with PyAutoGUI functions.
Copyright (c) 2020, Brett Moan <brett.moan@gmail.com>
"""

__license__ = """
In order to integrate with the pacakge pyautogui, some of the functions are derived from _pyautogui_win.py at 
https://github.com/asweigart/pyautogui/blob/6bfa7a23b8ccba80d3211a473d7c496ff869d3a2/pyautogui/_pyautogui_win.py

Therefore, this file is under BSD 3-clause, in addition to the GPL clause for this project.

Modifications are Copyright (c) 2020, BrettMoan

Original code from https://github.com/asweigart/pyautogui/blob/6bfa7a23b8ccba80d3211a473d7c496ff869d3a2/pyautogui/_pyautogui_win.py
Copyright (c) 2014, Al Sweigart
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the PyAutoGUI nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pyautogui import isShiftCharacter
from pyautogui._pyautogui_win import keyboardMapping
from pyautoeios.eios import EIOS
from pyautoeios.hexcodes import VK_LBUTTON, VK_RBUTTON, VK_MBUTTON

eios_obj = None
"""Global Shared Memory pointer used to interact with the RemoteLib"""

def _position():
    """compatibility wrapper for pyautogui."""
    return EIOS._EIOS_GetMousePosition(eios_obj)


def _word_to_mouse_button(word: str):
    """helper function in compatibility wrapper for pyautogui"""
    if word == "left":
        return VK_LBUTTON
    if word == "middle":
        return VK_MBUTTON
    if word == "right":
        return VK_RBUTTON

    raise ValueError("button argument not in ('left', 'middle', 'right')")


def _click(x, y, button):
    """compatibility wrapper for pyautogui."""
    _button = _word_to_mouse_button(button)
    EIOS._EIOS_HoldMouse(eios_obj, x, y, _button)
    EIOS._EIOS_ReleaseMouse(eios_obj, x, y, _button)


def _mouseDown(x, y, button):
    """pyautogui wrapper for _position."""
    _button = _word_to_mouse_button(button)
    EIOS._EIOS_HoldMouse(eios_obj, x, y, _button)


def _mouseUp(x, y, button):
    """pyautogui wrapper for _position."""
    _button = _word_to_mouse_button(button)
    EIOS._EIOS_ReleaseMouse(eios_obj, x, y, _button)


def _keyDown(key):
    """
    compatibility wrapper for pyautogui.
    
    modified from windows verison in pyautogui._pyautogui_win
    """
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    needsShift = isShiftCharacter(key)
    mods, vkCode = divmod(keyboardMapping[key], 0x100)

    for apply_mod, vk_mod in [
        (mods & 4, 0x12),
        (mods & 2, 0x11),
        (mods & 1 or needsShift, 0x10),
    ]:  # HANKAKU not suported! mods & 8
        if apply_mod:
            EIOS._EIOS_HoldKey(eios_obj, vk_mod)
    EIOS._EIOS_HoldKey(eios_obj, vkCode)
    for apply_mod, vk_mod in [
        (mods & 1 or needsShift, 0x10),
        (mods & 2, 0x11),
        (mods & 4, 0x12),
    ]:  # HANKAKU not suported! mods & 8
        if apply_mod:
            EIOS._EIOS_ReleaseKey(eios_obj, vk_mod)


def _keyUp(key):
    """
    compatibility wrapper for pyautogui.

    modified from windows verison in pyautogui._pyautogui_win
    """
    if key not in keyboardMapping or keyboardMapping[key] is None:
        return

    needsShift = isShiftCharacter(key)
    mods, vkCode = divmod(keyboardMapping[key], 0x100)

    for apply_mod, vk_mod in [
        (mods & 4, 0x12),
        (mods & 2, 0x11),
        (mods & 1 or needsShift, 0x10),
    ]:  # HANKAKU not suported! mods & 8
        if apply_mod:
            EIOS._EIOS_HoldKey(eios_obj, vk_mod)
    EIOS._EIOS_ReleaseKey(eios_obj, vkCode)
    for apply_mod, vk_mod in [
        (mods & 1 or needsShift, 0x10),
        (mods & 2, 0x11),
        (mods & 4, 0x12),
    ]:  # HANKAKU not suported! mods & 8
        if apply_mod:
            EIOS._EIOS_ReleaseKey(eios_obj, vk_mod)


def _moveTo(x, y):
    """compatibility wrapper for pyautogui."""
    EIOS._EIOS_MoveMouse(eios_obj, x, y)


def _scroll(clicks, x=None, y=None):
    """
    compatibility wrapper for pyautogui.

    modified from windows verison in pyautogui._pyautogui_win
    """
    startx, starty = _position()
    width, height = _size()

    if x is None:
        x = startx
    else:
        if x < 0:
            x = 0
        elif x >= width:
            x = width - 1
    if y is None:
        y = starty
    else:
        if y < 0:
            y = 0
        elif y >= height:
            y = height - 1

    EIOS._EIOS_ScrollMouse(eios_obj, x, y, clicks)


def _hscroll(clicks, x, y):
    """compatibility wrapper for pyautogui."""
    return _scroll(clicks, x, y)


def _vscroll(clicks, x, y):
    """compatibility wrapper for pyautogui."""
    return _scroll(clicks, x, y)


def _size():
    """compatibility wrapper for pyautogui."""
    return EIOS._EIOS_GetTargetDimensions(eios_obj)
