import time
import pyautoeios as pyauto
_client = pyauto.eios.EIOS()
pyauto.pair_client(_client)
print(time.monotonic())
_client.send_string("hello from the other side.", 80, 25)
print(time.monotonic())
