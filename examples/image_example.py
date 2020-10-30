import os
import pyautoeios as pyauto

pyauto.pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True

pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    box = pyauto.locateOnScreen(image=os.path.join('examples','TUphiXbRhV.png'), confidence=0.999)
    pyauto.moveTo(box)
