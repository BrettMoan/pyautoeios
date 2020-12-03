#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.

import ctypes
from io import StringIO
from html.parser import HTMLParser

from pyautoeios.eios import (
    EIOS,
    SIZE,
    CHAR,
    BYTE,
    BOOL,
    SHORT,
    INT,
    LONG,
    FLOAT,
    DOUBLE,
    STRING,
    OBJECT,
)
from pyautoeios.eios_meta import Type


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class RSType:
    def __init__(self, eios: EIOS = None, ref=None):
        self.eios = eios
        self.ref = ref
        if self.ref:
            eios._objects[eios._pid][ref] = eios._objects[eios._pid].get(ref, 0) + 1
            if self.ref in self.eios._untracked[self.eios._pid]:
                self.eios._untracked[self.eios._pid].pop(self.ref)

    def __str__(self):
        return f"{self.__class__.__name__}({self.ref}) paired with {self.eios}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ref}) paired with {self.eios}"

    def __del__(self):
        if self.ref:
            objects = self.eios._objects.get(self.eios._pid)
            if not objects:
                return
            ref_count = objects.get(self.ref)
            # print(f"{self.ref = } , {ref_count = }")
            if ref_count == 1:
                self.eios._objects[self.eios._pid].pop(self.ref)
                self.eios.release_object(self.ref)
            if ref_count > 1:
                self.eios._objects[self.eios._pid][self.ref] -= 1


class RSArray(RSType):
    def __init__(
        self,
        eios: EIOS = None,
        ref=None,
        size=None,
        arr_type: Type = None,
        indices=None,
    ):
        self.elements = None
        self.size = size
        self.arr_type = arr_type
        super().__init__(eios, ref)
        if indices:
            _elements = eios.get_array_indices(ref, self.arr_type, indices)
            self.size = len(indices)
            self.elements = [self[i] for i in indices]
            # _type = self.ctype * self.size
            # self.elements = ctypes.cast(_elements, ctypes.POINTER(_type)).contents

    def __getitem__(self, key: int = None):
        if self.elements:
            return self.elements[key]
        element = self.eios.get_array_index_from_pointer(
            instance=self.ref, arr_type=self.arr_type, index=key
        )
        return element

    def all(self, refresh: bool = False):
        if refresh:
            del self.elements
        if not self.elements:
            if not self.size:
                self.size = self.eios.get_array_size(self.ref)
            self.elements = [self[i] for i in range(0, self.size)]
        return self.elements


class RSIntArray(RSArray):
    def __init__(
        self,
        eios: EIOS = None,
        ref=None,
        size=None,
        indices=None,
    ):
        # print(
        #     f"eios={eios = }"
        #     f"ref={ref = }"
        #     f"size={size = }"
        #     f"arr_type={INT = }"
        #     f"indices={indices = }"
        # )
        super().__init__(
            eios=eios,
            ref=ref,
            size=size,
            arr_type=INT,
            indices=indices,
        )


class RSLongArray(RSArray):
    def __init__(
        self,
        eios: EIOS = None,
        ref=None,
        size=None,
        indices=None,
    ):
        super().__init__(
            eios=eios,
            ref=ref,
            size=size,
            arr_type=LONG,
            indices=indices,
        )


class RSObjectArray(RSArray):
    def __init__(
        self,
        eios: EIOS = None,
        ref=None,
        size=None,
        indices=None,
    ):
        super().__init__(
            eios=eios,
            ref=ref,
            size=size,
            arr_type=OBJECT,
            indices=indices,
        )


class RSStringArray(RSArray):
    def __init__(
        self,
        eios: EIOS = None,
        ref=None,
        size=None,
        indices=None,
    ):
        super().__init__(
            eios=eios,
            ref=ref,
            size=size,
            arr_type=STRING,
            indices=indices,
        )

    # def __getitem__(self, key: int = None):
    #     element = self.eios.Reflect_Array_Index(self.ref, self.ra_type, key, 1)
    #     length = ctypes.cast(element, ctypes.POINTER(ctypes.c_int32)).contents.value
    #     return strip_tags(
    #         ctypes.string_at(element, length + 4)[4:]
    #         .replace(b"\xc2\xa0", b" ")
    #         .decode("utf8")
    #     )


def get_rs_int_array(eios, ref=None, hook=None, max_size=None):
    _ref, size = eios.get_array_with_size(ref, hook)
    if _ref and size:
        if max_size:
            size = min(size, max_size)
        return RSIntArray(eios, _ref, size).all()
    return None


def get_rs_string_array(eios, ref=None, hook=None, max_size=None):
    _ref, size = eios.get_array_with_size(ref, hook)
    if _ref and size:
        if max_size:
            size = min(size, max_size)
        return RSStringArray(eios, _ref, size).all()
    return None

def get_rs_object_array(eios, ref=None, hook=None, max_size=None):
    _ref, size = eios.get_array_with_size(ref, hook)
    if _ref and size:
        if max_size:
            size = min(size, max_size)
        return RSObjectArray(eios, _ref, size).all()
    return None
