import pyautoeios as pyauto

pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    im = pyauto.screenshot(imageFilename="im.show()")
