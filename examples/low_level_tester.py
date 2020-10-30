import getpass
import time
from pyautoeios.eios import EIOS
from pyautoeios.hexcodes import VK_ESC, VK_LBUTTON

print("injecting into client")
# Create instance of Remote Input
reflect = EIOS()

# Get number of clients
client_count = reflect._EIOS_GetClients()
print(f"there are {client_count} clients")

# Get first clients PID
client_pid = reflect._EIOS_GetClientPID(0)

# Pair the client and get the target or eios_ptr
print(f"Pointer for the target for client is = {reflect._eios_ptr}")

reflect.lose_focus()
have_focus1 = reflect.has_focus()
print(f"have_focus1 = {have_focus1}")

reflect.gain_focus()
have_focus2 = reflect.has_focus()
print(f"have_focus2 = {have_focus2}")

dimensions = reflect.get_target_dimensions()
print(f"dimensions = {dimensions}")

mouse_position = reflect.get_mouse_position()
print(f"mouse_position = {mouse_position}")

real_mouse_position = reflect.get_real_mouse_position()
print(f"real_mouse_position = {real_mouse_position}")

print(
    "If you're at the login screen enter password to do a stupidly simple login script with fixed coordinates"
)
password = getpass.getpass()
if password:
    reflect.hold_key(VK_ESC)
    time.sleep(0.3)
    reflect.release_key(VK_ESC)
    reflect.hold_key(VK_ESC)
    time.sleep(0.3)
    reflect.release_key(VK_ESC)
    reflect.hold_key(VK_ESC)
    time.sleep(0.3)
    reflect.release_key(VK_ESC)

    reflect._EIOS_MoveMouse(478, 294)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

    reflect._EIOS_HoldMouse(478, 294, VK_LBUTTON)
    time.sleep(0.3)
    reflect._EIOS_ReleaseMouse(478, 294, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

    reflect._EIOS_HoldMouse(375, 263, VK_LBUTTON)
    time.sleep(0.3)
    reflect._EIOS_ReleaseMouse(375, 263, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

    reflect._EIOS_SendString(password, 100, 100)

    reflect._EIOS_HoldMouse(329, 319, VK_LBUTTON)
    time.sleep(0.3)
    reflect._EIOS_ReleaseMouse(329, 319, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position()
    print(f"mouse_position = {mouse_position}")

reflect.lose_focus()
