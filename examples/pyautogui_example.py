
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
    pyauto.typewrite(getpass.getpass(), interval=0.7)
    im = pyauto.screenshot()
    im.show()
    click_on_spot_in_box(Box(left=238, top=301, width=148,height=41))



