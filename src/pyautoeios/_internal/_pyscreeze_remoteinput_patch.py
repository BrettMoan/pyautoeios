"""This module patches pyscreeze to allow transparent needles on the opencv searches.
Copyright (c) 2020, Brett Moan <brett.moan@gmail.com>
"""

__license__ = """
Copyright 2020 by Brett J. Moan

This file is part of pyautoeios.

pyautoeios is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyautoeios is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.

In order to integrate with the package PyScreeze, some of the functions
are derived from pyscreeze/__init__.py at
<https://github.com/asweigart/pyscreeze/blob/master/pyscreeze/__init__.py>

Therefore, this file is also under BSD 3-clause, in addition to version 3 of the
GPL. Note the GPLv3 is more restrictive than the BSD 3-clause. Be sure to study
both licenses.

Original code from
<https://github.com/asweigart/pyscreeze/blob/master/pyscreeze/__init__.py>
Copyright (c) 2014, Al Sweigart
All rights reserved.

Modifications are Copyright (c) 2020, Brett J. Moan
All rights reserved.

# The BSD 3-clause:

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the PyScreeze nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import numpy as np
from PIL import Image

from pyautoeios.eios import EIOS

eios_obj = None
"""Global Shared Memory pointer used to interact with the RemoteLib"""


def _screenshot_remoteinput(imageFilename=None, region=None):
    """compatibility wrapper for pyautogui."""
    buffer = EIOS.get_image_buffer(eios_obj)
    x, y = EIOS.get_target_dimensions(eios_obj)
    np_image = np.asarray(buffer[: x * y * 4]).reshape((y, x, 4))
    im = Image.fromarray(np_image[:, :, :3].astype(np.uint8)[:, :, ::-1])

    if region is not None:
        assert len(region) == 4, "region argument must be a tuple of four ints"
        region = [int(x) for x in region]
        im = im.crop(
            (region[0], region[1], region[2] + region[0], region[3] + region[1])
        )
    if imageFilename == "im.show()":
        im.show()
    elif imageFilename is not None:
        im.save(imageFilename)
    return im
