import os
import sys

import numpy

from .BBox import BBox

class ImageMeta(BBox):

	'''
	Implement an Image meta protocol, which is three things:
		1) Knowledge about position of an image (min, max, etc)
		2) Knowledge about the dimensions of an image's pixels/voxels
		3) Ability to ravel / unravel pixel to flat index
	'''