import sys
import os

import numpy

class BBox(object):
    '''
        Implementation of an abstract N dimensional bounding box
        Can be 2D, 3D, or N-D, since the implementation is all
        tied to numpy 1D arrays to manage the coordinates.
    '''

    def __init__(self, lower_point, upper_point):
        '''
        Initialize an instance of BBox.  Requires lower_point < upper_point
        '''

        self._lower_point = numpy.asarray(lower_point, dtype=numpy.float32)
        self._upper_point = numpy.asarray(upper_point, dtype=numpy.float32)

        if not self._valid(self._lower_point, self._upper_point):
            sys.stdout.write(self._validity_msg)
            raise Exception("Entered points are invalid: {} and {}".format(self._lower_point, self._upper_point))



    def _valid(self, _this_lower_p, _this_upper_p):

        self._validity_msg = ""
        # Enforce the two points are both 1D
        if len(_this_lower_p.shape) != 1 or len(_this_upper_p.shape) != 1:
            self._validity_msg = "Must supply 1D arrays for bounding box"
            return False

        if (_this_lower_p >= _this_upper_p).any():
            self._validity_msg = "lower_point must be less than upper point"
            return False

    def lower(self):
        return self._lower_point

    def upper(self):
        return self._upper_point


    def update(self, _dummy=None, lower_point=None, upper_point=None):
        if _dummy is not None:
            raise Exception("Must use keyword arguments to update")

        _new_lower_point = self._lower_point
        _new_upper_point = self._upper_point

        if lower_point is not None:
            _new_lower_point = lower_point
        if upper_point is not None:
            _new_upper_point = upper_point

        if self._valid(_new_lower_point, _new_upper_point):
            self._lower_point = _new_lower_point
            self._upper_point = _new_upper_point


    def center(self):
        return 0.5*(self._lower_point + self._upper_point)

    def dimensions(self):
        return self._upper_point - self._lower_point

    def area(self):
        return numpy.sum(self.dimensions()**2)  

    def overlap(self, other):
        pass

    def inclusive(self, other):
        pass

    def contains(self, point):
        '''
        Determine if a point is contained in this box or not
        '''

        _this_point = numpy.asarray(point)

        if _this_point.shape != self._lower_point.shape:
            raise Exception("Can not cast point to appropriate shape")

        if (_this_point < self._lower_point).any():
            return False
        if (_this_point > self._upper_point).any():
            return False

        pass

    def intersection(self, other):
        '''
        Return the box that is the intersection of both boxes, or None
        if the intersection is 0.
        
        '''
        
        # _new_lower_point = numpy.min(self._lower_point, other.lower())



        pass


    def union(self, other):
        '''
        Return the smallest box that contains both boxes
        '''



        pass


    def __str__(self):
        return "({}) -> ({})".format(
            ",".join(self._lower_point),
            ",".join(self._upper_point)
        )

