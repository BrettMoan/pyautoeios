from typing import List
from pyautoeios import eios
from pyautoeios import hexcodes

from pyautoeios import _pyscreeze_remoteinput_patch
from pyautoeios import _pyautogui_remoteinput_patch

import pyautogui
pyautogui.platformModule = _pyautogui_remoteinput_patch
pyautogui.screenshot = _pyscreeze_remoteinput_patch._screenshot_remoteinput

if pyautogui.pyscreeze.useOpenCV:
    from pyautoeios import _pyscreeze_cv2_patch
    pyautogui.pyscreeze._load_cv2 = _pyscreeze_cv2_patch._load_cv2
    pyautogui.pyscreeze._extract_alpha_cv2 = _pyscreeze_cv2_patch._extract_alpha_cv2
    pyautogui.pyscreeze._locateAll_opencv = _pyscreeze_cv2_patch._locateAll_opencv

# now that we've patched  pyautogui lets do simulate a `from pyuautogui import *`
for attr in dir(pyautogui):
    if not attr.startswith('__'): 
        globals()[attr] = getattr(pyautogui, attr)

clients = []

def inject_clients() -> List[eios.EIOS]:
    try:
        while True:
            clients.append(eios.EIOS())
    except OSError:
        if len(clients) < 1:
            raise

def pair_client(eios_obj: eios.EIOS):
    _pyautogui_remoteinput_patch.eios_obj = eios_obj
    _pyscreeze_remoteinput_patch.eios_obj = eios_obj

__AUTHOR__ = "brett.moan@gmail.com"
__VERSION__ = "0.0.2"
