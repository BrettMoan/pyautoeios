import pyautogui
import _pyautogui_remoteinput

pyautogui.platformModule = _pyautogui_remoteinput
reflect = pyautogui.platformModule.REFLECT

reflect.EIOS_Inject()

# Get number of clients
client_count = reflect.EIOS_GetClients()
print(f"there are {client_count} clients")

# Get first clients PID
client_pid = reflect.EIOS_GetClientPID(0)

# Pair the client and get the target or eios_ptr
eios_ptr = reflect.EIOS_PairClient(client_pid)
print(f"Pointer for the target for client is = {eios_ptr}")

pyautogui.click(478, 294)
pyautogui.click(375, 263)
pyautogui.typewrite("password")
pyautogui.click(329, 319)
pyautogui.platformModule._size()
