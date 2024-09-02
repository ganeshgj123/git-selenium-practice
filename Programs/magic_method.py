# --------------------------------------------------------------------------------------
# magic.py
# -------------------------------------------------------------------------------------
# Container Protocol
# 1. __contains__
# 2. __len__
# 3. __getitem__
# 4. __setitem__
# 5. __delitem__

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __contains__(self, item):
        if item == self.a or item == self.b:
            return True
        return False

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.a
        if index == 1:
            return self.b
        raise IndexError("Point Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise IndexError("Point Index out of range")

    def __delitem__(self, index):
        ...


class PositivePoint(Point):
    def __setitem__(self, index, value):
        if value < 0:       # extra functionality
            raise ValueError("Negative values not allowed")
        super().__setitem__(index, value)


# range of 0th index is 0-50
# range of 1st index is 1-100
class RangePoint(Point):
    def __setitem__(self, index, value):
        if index == 0:
            if value >= 0 and value <= 50:
                super().__setitem__(index, value)
            else:
                raise ValueError("Value out or range")
        elif index == 1:
            if value >= 0 and value <= 100:
                super().__setitem__(index, value)
            else:
                raise ValueError("Value out or range")
        else:
            raise IndexError("Index out of range")


class Point:
    def __init__(self, *values):
        self.items = [ ]
        for value in values:
            self.items.append(value)
    
    def __len__(self):
        return len(self.items)      # self.items.__len__()

    def __contains__(self, item):
        if item in self.items:
            return True
        return False

    def __getitem__(self, index):
        return self.items[index]        # items.__getitem__(index)

    def __setitem__(self, index, value):
        self.items[index] = value       # items.__setitem__(index, value)

# ----------------------------------------------------------
# Attribute Protocol
# ----------------------------------------------------------
# 1. __getattribute__(self, name)
# 2. __setattr__(self, name, value)
# 3. __delattr__(self, name)
class Point:
    def __init__(self, a, b):
        self.a = a      # p.a = 1
        self.b = b      # p.b = -1
    
    # over-riding
    def __setattr__(self, name, value):
        print(f"setting the attribute {name} to {value}")
        if value < 0:
            raise ValueError("NO")
        super().__setattr__(name, value)


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, name, value):
        super().__setattr__(name, value.upper())



class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, name, value):
        super().__setattr__(name, value[::-1])

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


class Employee:
    def __init__(self, fname, lname, pay):
        super().__setattr__("fname", fname)
        super().__setattr__("lname", lname)
        super().__setattr__("pay", pay)

    def __setattr__(self, name, value):
        raise AttributeError("No")

    def __delattr__(self, name):
        raise AttributeError("No You cannot delete an attribute")

