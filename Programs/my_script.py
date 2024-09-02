from descriptor2 import ValidateAge, ValidatePay, ValidateFname, ValidateLname

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
