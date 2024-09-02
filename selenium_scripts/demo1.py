# 0, 1, 2, 3, 4
class Log:
    def __init__(self, level):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value not in (0, 1, 2, 3, 4):
            raise ValueError("allowd values are (0, 1, 2, 3, 4)")
        self._level = value

    def log(self, message):
        ...



class Number:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Only Numbers are allowed")
        obj.__dict__[self.name] = value

class Arithmetic:
    a = Number("_a")
    b = Number("_b")
    c = Number("_c")
    d = Number("_d")
    e = Number("_e")

    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise ValueError("only numbers are allowed")
        super().__setattr__(name, value)


#    @property
#    def a(self):
#        return self._a
#
#    @a.setter
#    def a(self, value):
#        if not isinstance(value, (int, float)):
#            raise ValueError("Only numbers are allowed")
#        self._a = value
#
#    @property
#    def b(self):
#        return self._b
#
#    @b.setter
#    def b(self, value):
#        if not isinstance(value, (int, float)):
#            raise ValueError("Only numbers are allowed")
#        self._b = value
#
#    @property
#    def c(self):
#        return self._c
#
#    @c.setter
#    def c(self, value):
#        if not isinstance(value, (int, float)):
#            raise ValueError("Only numbers are allowed")
#        self._c = value
#
#    @property
#    def d(self):
#        return self._d
#
#    @d.setter
#    def d(self, value):
#        if not isinstance(value, (int, float)):
#            raise ValueError("Only numbers are allowed")
#        self._d = value
