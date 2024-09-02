# desc.py
# -------------------------------
# Descriptor protocol
# --------------------------------
#class Demo:
#    def __init__(self, private_variable):
#        self.private_variable = private_variable
#
#    def __get__(self, obj, cls):
#        print(f"Getting the value of {self.private_variable}")
#        return obj.__dict__[self.private_variable]      # e.__dict__["_fname"]
#
#    def __set__(self, obj, value):
#        print(f"setting {self.private_variable} to {value}")
#        obj.__dict__[self.private_variable] = value

class Validate:
    def __get__(self, obj, cls):
        return obj.__dict__[self.private_name]

class Number(Validate):
    def __init__(self, private_name, *, min_value, max_value):
        self.private_name = private_name
        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("only numbers are allowed")
        if value < self.min_value:
            raise ValueError(f"Min value should be {self.min_value}")
        if value > self.max_value:
            raise ValueError(f"Max value should be {self.max_value}")
        obj.__dict__[self.private_name] = value

class String(Validate):
    def __init__(self, private_name, *, min_len, max_len):
        self.private_name = private_name
        self.min_len = min_len
        self.max_len = max_len

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("only strings are allowed")
        if len(value) < self.min_len:
            raise ValueError(f"Min len should be {self.min_len}")
        if len(value) > self.max_len:
            raise ValueError(f"Max len should be {self.max_len}")
        obj.__dict__[self.private_name] = value


class ValidateAge(Number):
    pass

class ValidatePay(Number):
    pass

class ValidateFname(String):
    pass

class ValidateLname(String):
    pass

class Employee:
    fname = ValidateFname("_fname", min_len=4, max_len=8)
    lname = ValidateLname("_lname", min_len=5, max_len=12)
    pay = ValidatePay("_pay", min_value=1000, max_value=90000)
    age = ValidateAge("_age", min_value=18, max_value=60)

    def __init__(self, fname, lname, pay, age):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.age = age
