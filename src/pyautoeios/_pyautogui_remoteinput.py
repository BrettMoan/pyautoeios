""" This module integrates remoteinput's EIOS methods with pyautogui.

some of the functions are derived from _pyautogui_win.py at 
https://github.com/asweigart/pyautogui/blob/6bfa7a23b8ccba80d3211a473d7c496ff869d3a2/pyautogui/_pyautogui_win.py

"""
# EIOS implementation of PyAutoGUI functions.
# BSD license
# Brett Moan brett.moan+pyautoschool@gmail.com
from pyautogui import isShiftCharacter
from pyautogui._pyautogui_win import keyboardMapping
from pyautoeios.eios import EIOS

EIOS_PTR = None
VK_LBUTTON = 0x01  # Left mouse button
VK_RBUTTON = 0x02  # Right mouse button
VK_MBUTTON = 0x04  # Middle mouse button (three-button mouse)


def _position():
    """compatibility wrapper for pyautogui."""
    return EIOS._EIOS_GetMousePosition(EIOS_PTR)


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
    EIOS._EIOS_HoldMouse(EIOS_PTR, x, y, _button)
    EIOS._EIOS_ReleaseMouse(EIOS_PTR, x, y, _button)


def _mouseDown(x, y, button):
    """pyautogui wrapper for _position."""
    _button = _word_to_mouse_button(button)
    EIOS._EIOS_HoldMouse(EIOS_PTR, x, y, _button)


def _mouseUp(x, y, button):
    """pyautogui wrapper for _position."""
    _button = _word_to_mouse_button(button)
    EIOS._EIOS_ReleaseMouse(EIOS_PTR, x, y, _button)


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
            EIOS._EIOS_HoldKey(EIOS_PTR, vk_mod)
    EIOS._EIOS_HoldKey(EIOS_PTR, vkCode)
    for apply_mod, vk_mod in [
        (mods & 1 or needsShift, 0x10),
        (mods & 2, 0x11),
        (mods & 4, 0x12),
    ]:  # HANKAKU not suported! mods & 8
        if apply_mod:
            EIOS._EIOS_ReleaseKey(EIOS_PTR, vk_mod)


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
            EIOS._EIOS_HoldKey(EIOS_PTR, vk_mod)
    EIOS._EIOS_ReleaseKey(EIOS_PTR, vkCode)
    for apply_mod, vk_mod in [
        (mods & 1 or needsShift, 0x10),
        (mods & 2, 0x11),
        (mods & 4, 0x12),
    ]:  # HANKAKU not suported! mods & 8
        if apply_mod:
            EIOS._EIOS_ReleaseKey(EIOS_PTR, vk_mod)


def _moveTo(x, y):
    """compatibility wrapper for pyautogui."""
    EIOS._EIOS_MoveMouse(EIOS_PTR, x, y)


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

    EIOS._EIOS_ScrollMouse(EIOS_PTR, x, y, clicks)


def _hscroll(clicks, x, y):
    """compatibility wrapper for pyautogui."""
    return _scroll(clicks, x, y)


def _vscroll(clicks, x, y):
    """compatibility wrapper for pyautogui."""
    return _scroll(clicks, x, y)


def _size():
    """compatibility wrapper for pyautogui."""
    return EIOS._EIOS_GetTargetDimensions(EIOS_PTR)
