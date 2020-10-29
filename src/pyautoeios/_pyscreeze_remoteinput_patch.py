"""This module patches pyscreeze to allow transparent needles on the opencv searches.
Copyright (c) 2020, Brett Moan <brett.moan@gmail.com>
"""

__license__ = """
These are patches to the an original file found at 
https://github.com/asweigart/pyscreeze/blob/master/pyscreeze/__init__.py

Therefore, this file is under the BSD 3-clause from that project

Modifications are Copyright (c) 2020, BrettMoan

Original code from https://github.com/asweigart/pyscreeze/blob/master/pyscreeze/__init__.py
Copyright (c) 2014, Al Sweigart
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of PyScreeze nor the names of its
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
    np_image = np.asarray(buffer[:x * y * 4]).reshape((y, x, 4))[:,:,:3].astype(np.uint8)
    im = Image.fromarray(np_image[:,:,::-1])
    if region is not None:
        assert len(region) == 4, 'region argument must be a tuple of four ints'
        region = [int(x) for x in region]
        im = im.crop((region[0], region[1], region[2] + region[0], region[3] + region[1]))
    if imageFilename is not None:
        im.save(imageFilename)
    return im


