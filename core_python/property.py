# -*- coding: utf-8 -*-

class HideX(object):

    def __init__(self, x):
        self.x = x

    def get_x(self):
        return ~self.__x

    def set_x(self, x):
        assert isinstance(x, int), \
                "x must be an integer"
        self.__x = ~x

    x = property(get_x, set_x)

class HideY(object):

    def __init__(self):
        self._x = None

    @property
    def x(self):
        """ propety x"""
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @x.deleter
    def x(self):
        del self._x


tx = HideX(10)
print tx.__class__.__dict__.keys()
print tx.__class__.__mro__

ty = HideY()
ty.x=30
print ty.x
print ty.__class__.__dict__.keys()
print ty.__class__.__mro__


