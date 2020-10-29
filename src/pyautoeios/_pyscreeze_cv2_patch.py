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

import cv2
import numpy

def _load_cv2(img, grayscale=None, alpha=False):
    """
    TODO
    """
    # load images if given filename, or convert as needed to opencv
    # Alpha layer just causes failures at this point, so flatten to RGB.
    # RGBA: load with -1 * cv2.CV_LOAD_IMAGE_COLOR to preserve alpha
    # to matchTemplate, need template and image to be the same wrt having alpha

    if grayscale is None:
        grayscale = GRAYSCALE_DEFAULT
    if isinstance(img, (str, unicode)):
        # The function imread loads an image from the specified file and
        # returns it. If the image cannot be read (because of missing
        # file, improper permissions, unsupported or invalid format),
        # the function returns an empty matrix
        # http://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html
        if alpha:
            img_cv = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        elif grayscale:
            img_cv = cv2.imread(img, LOAD_GRAYSCALE)
        else:
            img_cv = cv2.imread(img, LOAD_COLOR)
        if img_cv is None:
            raise IOError("Failed to read %s because file is missing, "
                          "has improper permissions, or is an "
                          "unsupported or invalid format" % img)
    elif isinstance(img, numpy.ndarray):
        # don't try to convert an already-gray image to gray
        if grayscale and len(img.shape) == 3:  # and img.shape[2] == 3:
            img_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img_cv = img
    elif hasattr(img, 'convert'):
        # assume its a PIL.Image, convert to cv format
        img_array = numpy.array(img.convert('RGB'))
        img_cv = img_array[:, :, ::-1].copy()  # -1 does RGB -> BGR
        if grayscale:
            img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    else:
        raise TypeError('expected an image filename, OpenCV numpy array, or PIL image')
    return img_cv

def _extract_alpha_cv2(img, hardedge = True):
    """ assigns a solid white/black to a mask based off of the alpha channel, then converts the image to COLOR_BGRA2BGR"""

    # [:,:,3] returns the alpha channel. we could also use  cv2.split(img)[3], but split is a costly operation (in terms of time), 
    # so only use it if necessary. Numpy indexing is much more efficient and should be used if possible.
    mask = numpy.array(img[:,:,3])
    
    # 
    if hardedge: 
        mask[0][ mask[0] <= 128 ] = 0
        mask[0][ mask[0] >  128 ] = 255


    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    return img, mask



def _locateAll_opencv(needleImage, haystackImage, grayscale=None, limit=10000, region=None, step=1,
                      confidence=0.999, alpha=False, method=cv2.TM_CCOEFF_NORMED):
    """
    TODO - rewrite this
        faster but more memory-intensive than pure python
        step 2 skips every other row and column = ~3x faster but prone to miss;
            to compensate, the algorithm automatically reduces the confidence
            threshold by 5% (which helps but will not avoid all misses).
        limitations:
          - OpenCV 3.x & python 3.x not tested
          - RGBA images are treated as RBG (ignores alpha channel unless alpha keyword is used, then needle can use alpha channel)
          - OpenCV hasn't impelmented alpha transparent matching except on two methods cv2.TM_SQDIFF and cv2.TM_CCORR_NORMED
            https://stackoverflow.com/questions/35658323/python-opencv-matchtemplate-is-mask-feature-implemented
           
    """
    if grayscale is None:
        grayscale = GRAYSCALE_DEFAULT

    confidence = float(confidence)

    needleImage = _load_cv2(needleImage, grayscale=grayscale, alpha=alpha)
    needleHeight, needleWidth = needleImage.shape[:2]
    haystackImage = _load_cv2(haystackImage, grayscale=grayscale)

    if region:
        haystackImage = haystackImage[region[1]:region[1]+region[3],
                                      region[0]:region[0]+region[2]]
    else:
        region = (0, 0)  # full image; these values used in the yield statement
    if (haystackImage.shape[0] < needleImage.shape[0] or
        haystackImage.shape[1] < needleImage.shape[1]):
        # avoid semi-cryptic OpenCV error below if bad size
        raise ValueError('needle dimension(s) exceed the haystack image or region dimensions')

    if step == 2:
        confidence *= 0.95
        needleImage = needleImage[::step, ::step]
        haystackImage = haystackImage[::step, ::step]
    else:
        step = 1

        
    if alpha and needleImage.shape[2] > 3:
        needleImage, transparent_mask = _extract_alpha_cv2(needleImage)
        result = cv2.matchTemplate(haystackImage, needleImage, method, mask = transparent_mask)

    else:
        result = cv2.matchTemplate(haystackImage, needleImage, method)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        match_condition = result < confidence
    else:
        match_condition = result > confidence

    # get all matches at once, credit: https://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image/9253805#9253805
    match_indices = numpy.arange(result.size)[(match_condition).flatten()]
    matches = numpy.unravel_index(match_indices[:limit], result.shape)

    if len(matches[0]) == 0:
        if USE_IMAGE_NOT_FOUND_EXCEPTION:
            raise ImageNotFoundException('Could not locate the image (highest confidence = %.3f)' % result.max())
        else:
            return

    # use a generator for API consistency:
    matchx = matches[1] * step + region[0]  # vectorized
    matchy = matches[0] * step + region[1]
    for x, y in zip(matchx, matchy):
        yield Box(x, y, needleWidth, needleHeight)