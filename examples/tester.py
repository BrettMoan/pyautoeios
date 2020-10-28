import getpass

from pyautoeios.eios import EIOS
from pyautoeios.hex_keycodes import VK_ESC, VK_LBUTTON

print("injecting into client")
# Create instance of Remote Input
reflect = EIOS()

# Get number of clients
client_count = reflect.EIOS_GetClients()
print(f"there are {client_count} clients")

# Get first clients PID
client_pid = reflect.EIOS_GetClientPID(0)

# Pair the client and get the target or eios_ptr
eios_ptr = reflect.EIOS_PairClient(client_pid)
print(f"Pointer for the target for client is = {eios_ptr}")

reflect.lose_focus(eios_ptr)
have_focus1 = reflect.has_focus(eios_ptr)
print(f"have_focus1 = {have_focus1}")

reflect.gain_focus(eios_ptr)
have_focus2 = reflect.has_focus(eios_ptr)
print(f"have_focus2 = {have_focus2}")

dimensions = reflect.get_target_dimensions(eios_ptr)
print(f"dimensions = {dimensions}")

mouse_position = reflect.get_mouse_position(eios_ptr)
print(f"mouse_position = {mouse_position}")

real_mouse_position = reflect.get_real_mouse_position(eios_ptr)
print(f"real_mouse_position = {real_mouse_position}")

print(
    "If you're at the login screen enter password to do a stupidly simple login _SCDECLpt with fixed coordinates"
)
password = getpass.getpass()
if password:
    reflect.hold_key(eios_ptr, VK_ESC)
    time.sleep(0.3)
    reflect.release_key(eios_ptr, VK_ESC)
    reflect.hold_key(eios_ptr, VK_ESC)
    time.sleep(0.3)
    reflect.release_key(eios_ptr, VK_ESC)
    reflect.hold_key(eios_ptr, VK_ESC)
    time.sleep(0.3)
    reflect.release_key(eios_ptr, VK_ESC)

    reflect._EIOS_MoveMouse(eios_ptr, 478, 294)
    mouse_position = reflect.get_mouse_position(eios_ptr)
    print(f"mouse_position = {mouse_position}")

    reflect._EIOS_HoldMouse(eios_ptr, 478, 294, VK_LBUTTON)
    time.sleep(0.3)
    reflect._EIOS_ReleaseMouse(eios_ptr, 478, 294, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position(eios_ptr)
    print(f"mouse_position = {mouse_position}")

    reflect._EIOS_HoldMouse(eios_ptr, 375, 263, VK_LBUTTON)
    time.sleep(0.3)
    reflect._EIOS_ReleaseMouse(eios_ptr, 375, 263, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position(eios_ptr)
    print(f"mouse_position = {mouse_position}")

    reflect._EIOS_SendString(eios_ptr, password, 100, 100)

    reflect._EIOS_HoldMouse(eios_ptr, 329, 319, VK_LBUTTON)
    time.sleep(0.3)
    reflect._EIOS_ReleaseMouse(eios_ptr, 329, 319, VK_LBUTTON)
    mouse_position = reflect.get_mouse_position(eios_ptr)
    print(f"mouse_position = {mouse_position}")

reflect._lose_focus(eios_ptr)
reflect._EIOS_ReleaseTarget(eios_ptr)
