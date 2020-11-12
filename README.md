# pyautoeios

Work in progress port remote_input from https://github.com/Brandon-T/Reflection to python

Design decision was made to implements patches to https://github.com/asweigart/pyautogui/ and github.com/asweigart/pyscreeze so
that the remote_input so that interface can be used.



Planned Features
  - [x] Works with python 3.8
  - [x] installable via pip
  - [x] Wraps well liked [pyautogui](https://github.com/asweigart/pyautogui/) interface
  - [x] Transparent Image finding when opencv is installed
  - [x] Injecting into multiple clients (so threads can be used for multi-boxing)
  - [x] no known memory leaks.

Backlog Features:
  - [ ] More examples?
  - [ ] Installs Dependancies for you (for now use the [Pipfile](/Pipfile))
  - [ ] integration of color and other methods https://github.com/BenLand100/srbot/tree/master/srbot
  - [ ] porting modules from https://github.com/SRL/SRL or https://github.com/ollydev/SRL-Development
  - [ ] porting of "reflection" modules from https://github.com/Brandon-T/Reflection

Current demo:

```python
import random
import getpass
from pyscreeze import Box
import pyautoeios as pyauto


def move_to_spot_in_box(box, **kwargs):
    print(f"box = {box}")
    if 'duration' not in kwargs:
        kwargs['duration'] = random.uniform(0.3,1.1)
    if 'tween' not in kwargs:
        kwargs['tween'] = pyauto.easeOutQuad

    cx,cy =  pyauto.center(box)
    x = random.randint(int(-1*(box.width/3)),int(box.width/3)) + cx
    y = random.randint(int(-1*(box.height/3)),int(box.height/3)) + cy
    print(f"x = {x}, y = {y}")
    pyauto.moveTo(x, y, **kwargs)


def click_on_spot_in_box(box, **kwargs):
    move_to_spot_in_box(box,**kwargs)
    pyauto.click(**kwargs)

pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    click_on_spot_in_box(Box(left=398, top=271, width=148, height=40))
    click_on_spot_in_box(Box(left=285, top=248, width=235, height=15))
    pyauto.typewrite(getpass.getpass(), interval=0.3)
    im = pyauto.screenshot()
    im.show()
    click_on_spot_in_box(Box(left=238, top=301, width=148,height=41))
```





Working: (tested with vanilla client)
    [x] EIOS_GainFocus
    [x] EIOS_GetClientPID
    [x] EIOS_GetClients
    [x] EIOS_GetMousePosition
    [x] EIOS_GetRealMousePosition
    [x] EIOS_GetTargetDimensions
    [x] EIOS_HasFocus
    [x] EIOS_HoldKey
    [x] EIOS_HoldMouse
    [x] EIOS_Inject
    [x] EIOS_LoseFocus
    [x] EIOS_MoveMouse
    [x] EIOS_PairClient
    [x] EIOS_ReleaseKey
    [x] EIOS_ReleaseMouse
    [x] EIOS_ReleaseTarget
    [x] EIOS_SendString

TODO:
    [ ] Functions that still need tested:
        [x] EIOS_GetImageBuffer
        [ ] EIOS_GetDebugImageBuffer
        [ ] EIOS_SetGraphicsDebugging
        [ ] EIOS_UpdateImageBuffer
        [ ] EIOS_ScrollMouse
        [x] EIOS_IsMouseButtonHeld
            ERRORS: can't import. throws the error:
            `AttributeError: function 'EIOS_IsMouseButtonHeld' not found`
        [ ] EIOS_IsKeyHeld
        [ ] EIOS_GetKeyboardSpeed
        [ ] EIOS_SetKeyboardSpeed
        [ ] EIOS_GetKeyboardRepeatDelay
        [ ] EIOS_SetKeyboardRepeatDelay
        [ ] EIOS_KillClientPID
        [ ] EIOS_KillClient
        [ ] EIOS_KillZombieClients
        [ ] Reflect_GetEIOS

    [ ] Functions that still need written:
        [x] Reflect_Object
        [ ] Reflect_IsSame_Object
        [ ] Reflect_InstanceOf
        [x] Reflect_Release_Object
        [ ] Reflect_Release_Objects
        [x] Reflect_Bool
        [x] Reflect_Char
        [x] Reflect_Byte
        [x] Reflect_Short
        [x] Reflect_Int
        [x] Reflect_Long
        [ ] Reflect_Float
        [ ] Reflect_Double
        [x] Reflect_String
        [ ] Reflect_Array
        [ ] Reflect_Array_With_Size
        [ ] Reflect_Array_Size
        [ ] Reflect_Array_Index
        [ ] Reflect_Array_Index2D
        [ ] Reflect_Array_Index3D
        [ ] Reflect_Array_Index4D
        [ ] Reflect_Array_Indices
