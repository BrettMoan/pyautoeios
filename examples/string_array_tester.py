import ctypes
import pyautoeios as pyauto
from pyautoeios import hooks

RI_STRING = 8

pyauto.inject_clients()

client = pyauto.clients[0]
print(f"{client = }")

_ref, size = client._Reflect_Array_With_Size(None, hooks.CLIENT_MENUACTIONS)
print(f"{_ref = }, {size = }")

for i in range(0, 500):
    result = client._Reflect_Array_Index(_ref, RI_STRING, i, 1)
    length = ctypes.cast(result, ctypes.POINTER(ctypes.c_int32)).contents.value
    # print(f"{i = }, {result = }, {ctypes.string_at(result) = }, {ctypes.wstring_at(result) = },  {pi = }, {pi.contents = }")
    print(f"{i = },{length = } {ctypes.string_at(result,length+4)[4:] = }")


# pascal = client._Pascal_Reflect_Array_Index(_ref, RI_STRING, 0, size)
# print(f'{pascal = }')


#######
# This is the same as the above, just using 2 dll calls, instead of the single `Reflect_Array_With_Size`
#######
# _ref2  = client._Reflect_Array(None, hooks.CLIENT_MENUOPTIONS)
# size2 = client._Reflect_Array_Size(_ref2)
# print(f"{_ref2 = }, {size2 = }")

# for i in range(0, size2):
#     result = client._Reflect_Array_Index(_ref2, RI_STRING, i, 1)
#     pi = ctypes.cast(result, ctypes.POINTER(ctypes.c_wchar))
#     print(f"{i = }, {result = }, {ctypes.string_at(result) = }, {ctypes.wstring_at(result) = },  {pi = }, {pi.contents = }")
