# demo.py
# ------------------------
# Object Oriented Design
#------------------------
class BankAccount:
    # common to all customers or instances 
    interest = 0.04     # class variable
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"Initial amount deposited {balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance = self.balance - amount
        self.transactions.append(f"Amount withdrawn {amount}")
        print(f"please collect the cash {amount}")

    def funds_transfer(self, to_account, amount):
        self.balance = self.balance - amount
        to_account.balance = to_account.balance + amount

    def statement(self):
        for transaction in self.transactions:
            print(transaction)
        print(f"Total Balance {self.balance}")

    def roi(self):
        amount = self.balance * self.__class__.interest
        self.balance = self.balance + amount
        self.transactions.append(f"Interest amount credited {amount}")


class SBAccount(BankAccount):
    # re-defining withdraw method in child
    def withdraw(self, amount):
        if amount > 500:        # this is the extra func that child is adding
            raise ValueError("Not allowed")
        super().withdraw(amount)


class SeniorCitizenAccount(BankAccount):
    interest = 0.05     # over-riding  or redefining
    def withdraw(self, amount):
        if amount > 1000:
            raise ValueError("No")
        super().withdraw(amount)


class SalaryAccount(BankAccount):
    MAX_DRAFT_AMOUNT = 10000
    FIRST_MONTH_BONUS = 1000

    def __init__(self, name):
        self.is_first_month_pay = True      # specific to child class
        self.draft_amount_taken = 0.0
        super().__init__(name, 0.00)     # passing parent class constructor args

    def deposit(self, amount):
        if self.is_first_month_pay:      # self.is_first_month_pay == True
            super().deposit(amount + SalaryAccount.FIRST_MONTH_BONUS)
            self.is_first_month_pay = False
        else:
            super().deposit(amount)

    def draft_amount(self, amount_requested):
        if self.draft_amount_taken + amount_requested > SalaryAccount.MAX_DRAFT_AMOUNT:
            raise ValueError("No")
        else:
            super().deposit(amount_requested)
            self.draft_amount_taken = self.draft_amount_taken + amount_requested


class SukanyaSamrudhiAccount(BankAccount):
    interest = 0.09
    def withdraw(self, amount):
        raise Exception("No")

    def funds_transfer(self, other, amount):
        raise Exception("No")


c1 = SukanyaSamrudhiAccount("steve", 1000)
c2 = SukanyaSamrudhiAccount("bill", 1000)





## Multi level Inheritance
#class A:
#    def demo(self):
#        print("A")
#
#class B(A):
#    def demo(self):
#        print("B")
#        super().demo()
#
#class C(B):
#    def demo(self):
#        print("C")
#        super().demo()
## --------------------------------------
"""MRO"""
## The order in which python will try to search for an attribute in Inheritance
## Hierarchy
#
#class Parent:
#    a = 10
#    def apple(self):
#        print(f"Parent {self.__class__.a}")     # d.__class__  # Demo.a   #Parent.a
#
#
#class Demo(Parent):
#    a = 20
#    def google(self):
#        print("Google")


































#class Demo:
#    def __init__(self, a):
#        self.a = a
#
#    def apple(self):
#        print(f"Running apple in Demo class {self.a}")
#
#    def google(self):
#        print(f"Running google in Demo class {self.a}")
#        self.apple()        # demo.apple(self)
## -----------------------------------------------------------------
##  Child inheriting from parent and child class has completely
## independent method (Yahoo)
#class Demo1(Demo):      # Demo1 extends Demo
#    def yahoo(self):
#        print(f"Running Yahoo in Demo1")
## -----------------------------------------------------------------
## Child inheriting from parent and child re-defines one of the attribute
## `apple` that is present in parent class (child over-rides apple that is in parent)
#class Demo2(Demo):
#   # over-riding the parent class `apple`
#    def apple(self):
#        print("Running apple in Demo2")
## -----------------------------------------------------------------
## Child inheriting from parent and child re-defines parent class `apple`
## adds some extra functionality and re-uses the parent class `apple` method
## functionality
#class Demo3(Demo):
#    def apple(self):
#        super().apple()     # Demo.apple(self)
#        print("Running apple in Demo3 adding some extra stuff")
#        # calling or re-using parent class functionality
#       # super() function is used to access any parent class attribute
## -----------------------------------------------------------------
## Child inheriting from parent and Child class has it's own constructor 
## attribute
#class Demo4(Demo):
#    def __init__(self, a, b):
#        self.b = b
#        super().__init__(a)     # initilising parent class constructor
#
#    def spam(self):
#        print(f"running spam in Demo4 {self.b}")
## -----------------------------------------------------------------



#class ShoppingCart:
#    # cls variable
#    prices = {"iPhone": 950, "iMac": 2500, "iWatch": 300, "iPad": 3500}
#    products = {"iPhone": 5, "iMac": 3, "iWatch": 2, "iPad": 3}
#
#    def __init__(self):
#        self.cart = [ ]
#
#    def add_item(self, name, quantity):
#        if name not in ShoppingCart.products:
#            raise Excecption("Invalid Product")
#        if quantity > ShoppingCart.products[name]:
#            raise Exception("Product out of stock")
#        item = {"name": name, "quantity": quantity, "price": ShoppingCart.prices[name]}
#        # item = (name, quantity, price)
#        self.cart.append(item)
#        # reduce the quantity of the product (reduce the stock)
#        ShoppingCart.products[name] = ShoppingCart.products[name] - quantity
#
#    
#    # calculates the totla cost of the cart 
#    def total(self):
#        _total = 0
#        for item in self.cart:
#            _total = _total + item["quantity"] * item["price"]
#        return _total
#
#
#    # removes some item from the cart
#    def remove_item(self, name):
#        for item in self.cart:
#            if name == item["name"]:
#                if item["quantity"] == 1:
#                    self.cart.remove(item)
#                else:
#                    item["quantity"] = item["quantity"] - 1
#
#
#c1 = ShoppingCart()
#c2 = ShoppingCart()
#c3 = ShoppingCart()
#
#c1.add_item("iPhone", 1)
#c1.add_item("iMac", 1)
#c1.add_item("iWatch", 2)























#class BankAccount:
#    # common to all customers or instances 
#    interest = 0.05     # class variable
#    def __init__(self, name, balance):
#        self.name = name
#        self.balance = balance
#        self.transactions = [ ]
#
#    def deposit(self, amount):
#        self.balance = self.balance + amount
#        self.transactions.append(f"Amount Deposited {amount}")
#
#    def withdraw(self, amount):
#        if amount > self.balance:
#            raise ValueError("Insufficient funds")
#        self.balance = self.balance - amount
#        self.transactions.append(f"Amount withdrawn {amount}")
#        print(f"please collect the cash {amount}")
#
#    def funds_transfer(self, to_account, amount):
#        self.balance = self.balance - amount
#        to_account.balance = to_account.balance + amount
#
#    def statement(self):
#        for transaction in self.transactions:
#            print(transaction)
#        print(f"Total Balance {self.balance}")
#
#    def roi(self):
#        amount = self.balance * BankAccount.interest
#        self.balance = self.balance + amount
#        self.transactions.append(f"Interest amount credited {amount}")
#
#
#c1 = BankAccount("steve", 1000)
#c2 = BankAccount("bill", 2000)




#class Point:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#    
#    # latest function will be taken You are over-writing __init__ variable
#    def __init__(self, a, b, c):
#        self.a = a
#        self.b = b
#        self.c = c
#
#p = Point(1, 2)
#
#
#class Point:
#    # overloaded constructor
#    def __init__(self, a=0, b=0, c=0):
#        self.a = a
#        self.b = b
#        self.c = c
#
#p1 = Point()
#p2 = Point(1)
#p3 = Point(1, 2)
#p4 = Point(1, 2, 3)



#class Player:
#    def __init__(self, x, y):
#        # instance data
#        self.x = x
#        self.y = y
#        self.health = 100
#
#    def move(self, dx, dy):
#        self.x = self.x + dx
#        self.y = self.y + dy
#    
#    # instance methods because it takes the data from instance dictionary
#    def attack(self, pts):
#        self.health = self.health - pts
#
#
#p1 = Player(0.1, 0.2)
#p2 = Player(0.5, 0.9)



# a = [1, 2]

#e1 = ("sandeep", "surayaprasad", 1000)
#e2 = ("steve", "jobs", 2000)


#e1 = {"fname": "steve", "lname": "jobs", "pay": 1000}
#e2 = {"fname": "sandeep", "lname": "suryaprasad", "pay": 2000}

#class Employee:
#    def __init__(self, fname, lname, pay):
#        self.fname = fname
#        self.lname = lname
#        self.pay = pay
#
#    def email(self):
#        return f"{self.fname}.{self.lname}@company.com"
#
#    def pay_hike(self, percentage_hike):
#        hike_amount = self.pay * percentage_hike
#        self.pay = self.pay + hike_amount
#
#e1 = Employee("steve", "jobs", 1000)
#e2 = Employee("bill", "gates", 2000)





#class Calculator:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#
#    def add(self):
#        return self.a + self.b
#
#    def sub(self):
#        return self.a - self.b
#
#    def mul(self):
#        return self.a * self.b
#
#    def div(self):
#        return self.a / self.b
#
## saving the data or creating an instance of Calculator class
#c1 = Calculator(1, 2)
#c2 = Calculator(4, 2)



# a = [1, 2]

# i want to add some delta amount to the items that are present in 1st and
# 2nd index of the above list
# indexing
#a[0] = a[0] + 0.5
#a[1] = a[1] + 0.5

# i want to add all the items that are present in the list
# indexing
# total = a[0] + a[1]

# i want to swap the items in the above list
# indexing
#temp = a[0]
#a[0] = a[1]
#a[1] = temp

# reset the values in the list
#a[0] = 0
#a[1] = 0

# custom container
#class Point:
#    # saving data inside `Point` class or container
#    def __init__(self, a, b):       # constructor
#        self.a = a
#        self.b = b
#
#    def move(self, dx, dy):
#        self.a = self.a + dx
#        self.b = self.b + dy
#
#    def reset(self):       # self = p1
#        # self is just a varaible and not a keyword or reserved word
#        # self will be internally pointing to one or the other instance 
#        # dictioanry
#        # self is also called as data
#        self.a = 0      # p2.a = 0
#        self.b = 0      # p2.b = 0
#
#    def swap(self):
#        temp = self.a
#        self.a = self.b
#        self.b = temp
#
#    def total(self):
#        return self.a + self.b
#
#p1 = Point(1, 2)
#p2 = Point(3, 4)
#p3 = Point(5, 6)
#
## Point.move(p2, 0.1, 0.1)
#p1.move(0.5, 0.5)       # Point.move(p1, 0.5, 0.5)


#a = [10, 20]
#b = [20, 30]
#
#def reset(data):
#    data[0] = 0
#    data[1] = 0
#
#reset(a)


# JAVA SYNTAX
#public class Point {
#    private int a;
#    private int b;
#    private int c;
#
#    public Point() {
#        this.Point(0, 0, 0)
#    }
#
#    public Point(a) {
#        this.Point(a, 0, 0)
#    }
#
#    public Point(a, b) {
#        this.Point(a, b, 0)
#    }
#
#    public Point(a, b, c) {
#        this.a = a
#        this.b = b
#        this.c = c
#    }
#}
#
#Point p1 = new Point()
#Point p2 = new Point(3, 4)


