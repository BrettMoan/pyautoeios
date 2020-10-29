# pyautoeios

Work in progress port remote_input from https://github.com/Brandon-T/Reflection to python

Design decision was made to implements patches to https://github.com/asweigart/pyautogui/ and github.com/asweigart/pyscreeze so
that the remote_input so that interface can be used.



Planned Features
  - [x] Works with python 3.8
  - [x] installable via pip
  - [ ] Installs Dependancies for you for now use the [](/Pipfile)
  - [x] Wraps well liked [pyautogui](https://github.com/asweigart/pyautogui/) interface
  - [x] Transparent Image finding when opencv is installed
  - [x] Injecting into multiple clients (so threads can be used for multi-boxing) 
  - [x] no known memory leaks.

Backlog Features:
  - [ ] More examples?
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

