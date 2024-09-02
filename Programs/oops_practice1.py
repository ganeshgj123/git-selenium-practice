class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a - self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b




c1 = Calculator(4, 3)

#print(Calculator.mul(c1))


##############################################################################################################

#Bank application

#1 deposit
#2 withdrawal
#3 fund_transfer
#4 roi
#5 statements


class BankApp:
    rate_of_interest = 0.04
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount Deposited {amount}")

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("insufficient balance")
        self.balance = self.balance - amount
        self.transactions.append(f"Amount Withdrawn {amount}")

    def fund_transfer(self,to_account, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance = self.balance - amount
        to_account.balance = to_account.balance + amount
        self.transactions.append(f"Amount Transferred {amount}")

    def bank_roi(self):
        amount = self.balance * BankApp.rate_of_interest
        self.balance = self.balance + amount
        self.transactions.append(f"Credited ROI amount {amount}")

    def statements(self):
        for transaction in self.transactions:
            print(transaction)

#
b1 = BankApp("Ganesh", 5000)
# b1.deposit(2000)
# b1.deposit(6000)
# b1.deposit(7000)
# b1.deposit(1000)
# b1.withdraw(5000)
# b1.bank_roi()
# b1.statements()
#print(b1.__dict__)
#
#
b2 = BankApp("Palmer",2000)
#
# b1.fund_transfer(b2,3000)
# b2.deposit(7000)
# b2.deposit(1000)
# b2.bank_roi()
#
# print("#"*100)
# b2.statements()
#
#print(b2.__dict__)


#print(BankApp.__dict__)



######################################################################################################

class ShoppingCart:

    def __init__(self):
        self.cart = []

    def add_item(self,name,quantity,price):
        item = {"name":name,"quantity":quantity,"price":price}
        self.cart.append(item)

    def remove_item(self,name):
        for item in self.cart:
            if item["quantity"] == 1:
                self.cart.remove(item)
            item["quantity"] = item["quantity"] - 1



class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, name, value):
        super().__setattr__(name,  value[::-1])


e1 = Employee("steve", "jobs")

#print(e1.fname,e1.lname)




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

        # self.fname = fname
        # self.lname = lname
        # self.pay = pay
        super().__setattr__("fname", fname)
        super().__setattr__("lname", lname)
        super().__setattr__("pay", pay)

    def __setattr__(self, name, value):
        raise AttributeError("No")

    def __delattr__(self, name):
        raise AttributeError("No You cannot delete an attribute")


e1 = Employee("ganesh","joshi",1000)

# print(e1.fname)




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


e1 = Employee("steve","40", 1000)
e2 = Employee("Elon","45", 1900)

# print(e1<e2)





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

employees = [e2, e4, e1, e3]

by_age = sorted(employees, key= lambda item: item.age)
#
# for item in by_age:
#     print(item.name,item.age)
#



# number protocol
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


p3 = p1 + p2


# print(p3)





"""
class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __bool__(self):
        if self.age >= 18:
            return True
        return False

    def __bool__(self):
         if self.pay >= 1000:
             return True
         return False



e = Employee("steve", 25, 999)
"""
"""
if e:
    print("hi")
else:
    print("bye")
"""



#object protocols

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
       print("__str__ getting called")
       return f"Point({self.a}, {self.b})"

    def __repr__(self):
       return f"Point({self.a}, {self.b})"


p1 = Point(1, 2)
p2 = Point(3, 4)

#print(p2.__dict__)


"""
class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    # def __str__(self):
    #     return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'


c = Ocean('Jellyfish', 5)

print(type(c))
"""



#
# import datetime
#
# mydate = datetime.datetime.now()
#
#
#
# print("__str__() string: ", type(mydate.__str__()))
# print("str() string: ", str(mydate))
#
# print("__repr__() string: ", type(mydate.__repr__()))
# print("repr() string: ", repr(mydate))
#


"""import datetime

mydate1 = datetime.datetime.now()
mydate2 = eval(repr(mydate1))

print(type(mydate1))
print( repr(mydate1))
print(repr(mydate2))

print("the values of the objects are equal: ", mydate1==mydate2)
"""




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

    def __enter__(self):
        print("__enter__ executing")
        return self

    def __exit__(self, exe_type, exe_value, traceback):
        print("__exit__ executing")
        print(exe_type)
        print(exe_value)
        print(traceback)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b



# with Calculator(2,0) as c:
#     print(c.div())
#











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


# with Timer() as t:
#     print(add(1, 2))
#




































