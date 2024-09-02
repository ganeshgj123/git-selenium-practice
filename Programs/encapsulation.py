# -------------------------------------------------------------------------------------
# _magic.py
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------
# data hiding
# =========================================================================
class Point_:
    def __init__(self, a, b):
        self.a = a      # p.a = 1
        self.b = b      # p.b = -1

#    def __setattr__(self, name, value):
#        if value < 0:
#            raise ValueError("Negative values not allowed")
#        super().__setattr__(name, value)

    # Getter Method
    @property
    def a(self):
        return self._a

    # Setter Method
    @a.setter
    def a(self, value):
        if value < 0:
            raise ValueError("Negative values not allowed for 'a'")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value < 0:
            raise ValueError("Negative values not allowed for 'b'")
        self._b = value





























class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # intercepting the values of "a" and "b"
    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only numbers are allowed")
        super().__setattr__(name, value)

    def mul(self):
        return self.a * self.b


class Circle:
    def __init__(self, radius):
        self.radius = radius        # c.radius = "3"

    def __setattr__(self, name, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Only Numbers are allowed for radius")
        super().__setattr__(name, value)

    def circumference(self):
        return 2 * 3.14 * self.radius


# 1. fname should be less than 5-8 characters
# 2. lname should be less than 8-12 characters
# 3. pay should be minimum $1000
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __setattr__(self, name, value):
        if name == "fname":
            if len(value) >= 5 and len(value) <= 8:
                super().__setattr__(name, value)
            else:
                raise ValueError("fname should be between 5 and 8 characters")
        elif name == "lname":
            if len(value) >=8 and len(value) <=12:
                super().__setattr__(name, value)
            else:
                raise ValueError("lname should be between 8 and 12 characters")
        elif name == "pay":
            if value < 1000:
                raise ValueError("minimum pay must be $1000")
            else:
                super().__setattr__(name, value)


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def __setattr__(self, name, value):
        if name not in ("fname", "lname", "pay"):
            raise AttributeError(f"Cannot set {name}")
        super().__setattr__(name, value)



