# -------------------------------------------------------------------------------------
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


# Comparision Protocol
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __gt__(self, other):
        if self.pay > other.pay:        # 1000 > 900    1000.__gt__(900)
            return True
        return False

    def __lt__(self, other):
        if self.pay < other.pay:
            return True
        return False

    def __eq__(self, other):
        if self.pay == other.pay:
            return True
        return False


class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __gt__(self, other):
       if self.age > other.age:        # 1000 > 900    1000.__gt__(900)
           return True
       return False

    def __lt__(self, other):
       if self.age < other.age:
           return True
       return False

    def __eq__(self, other):
       if self.age == other.age:
           return True
       return False


e1 = Employee("steve", 28, 1000)
e2 = Employee("bill", 26, 2000)
e3 = Employee("john", 18, 6000)
e4 = Employee("mark", 19, 7000)

employees = [e1, e2, e3, e4]


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __gt__(self, other):
        if self.a + self.b > other.a + other.b:
            return True
        return False

    def __lt__(self, other):
        if self.a + self.b < other.a + other.b:
            return True
        return False

    def __eq__(self, other):
        if self.a + self.b == other.a + other.b:
            return True
        return False


p1 = Point(1, 6)
p2 = Point(3, 4)


# Number protocol
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        n1 = self.a + self.b        # __add__ on int
        n2 = other.a + other.b
        return Point(n1, n2)

    def __sub__(self, other):
        n1 = self.a - self.b
        n2 = other.a - other.b
        return Point(n1, n2)

    def __mul__(self, other):
        n1 = self.a * self.b
        n2 = other.a * other.b
        return Point(n1, n2)

    def __truediv__(self, other):
        n1 = self.a / self.b
        n2 = other.a / other.b
        return Point(n1, n2)


p1 = Point(1, 2)
p2 = Point(2, 3)
# Point(3, 5)
# p3 = Point(3, 4)


# Truthiness protocol (__bool__ and __len__)
# first python will check if __bool__ is implemented or not
# if it is not implemented, __len__ will be called as fallback mechanism
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __bool__(self):
        print("__bool__")
        if self.a == 0 and self.b == 0:
            return False
        return True

class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __bool__(self):
        if self.age >= 18:
            return True
        return False

#    def __bool__(self):
#        if self.pay >= 1000:
#            return True
#        return False


p = Point(1, -1)
e = Employee("steve", 18, 1999)


#if e:
#    print("hi")
#else:
#    print("bye")


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

#    def __str__(self):
#        print("__str__ getting called")
#        return f"Point({self.a}, {self.b})"

    def __repr__(self):
        return f"Point({self.a}, {self.b})"

p1 = Point(1, 2)
p2 = Point(3, 4)


class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __repr__(self):
        return f"Employee({self.name}, {self.age}, {self.pay})"

    def __gt__(self, other):
       if self.age > other.age:        # 1000 > 900    1000.__gt__(900)
           return True
       return False

    def __lt__(self, other):
       if self.age < other.age:
           return True
       return False

    def __eq__(self, other):
       if self.age == other.age:
           return True
       return False


e1 = Employee("steve", 28, 1000)
e2 = Employee("bill", 26, 2000)
e3 = Employee("john", 18, 6000)
e4 = Employee("mark", 19, 7000)

employees = [e1, e2, e3, e4]





# Context manager Protocol
# __enter__ and __exit__

class Demo:
    def __enter__(self):
        print("__enter__ running")

    def __exit__(self, exe_type, exe_value, traceback):
        print("__exit__ running")


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def __enter__(self):
        print("__enter__ executing")
        return self

    def __exit__(self, exe_type, exe_value, traceback):
        print("__exit__ executing")
        print(exe_type)
        print(exe_value)
        print(traceback)


from time import time, sleep

def add(a, b):
    sleep(3)
    return a + b

def sub(a, b):
    sleep(4)
    return a - b


class Timer:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.elapsed = 0

    def __enter__(self):
        self.start = time()
        return self
        
    def __exit__(self, exe_type, exe_value, traceback):
        self.end = time()
        self.elapsed = self.end - self.start

with Timer() as t:
    print(add(1, 2))


