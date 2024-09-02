from datetime import datetime
from time import sleep


class A:

    f = 10
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    def demo(self):
        print("some sentence")
        print(A.f)
        print(self.__class__.f)
    def demo2(self):
        print("another sentence")
        self.demo()

class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d = d

    def demo3(self):
        print(B.f)
        print("anything")
        super().demo2()


#
# b= B(1,2,3,4)
# b.demo3()
#





###########################################################################

###########inheritance#######################

class BankAccount:
    interest_rate = 0.04

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("less amount not allowed")
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def transfer(self, to_account, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        to_account.deposit(amount)
        self.balance -= amount

    def roi(self):
        interest_amount = self.balance * self.__class__.interest_rate
        self.balance += interest_amount


class SavingsBankAccount(BankAccount):
    interest_rate = 0.05

    def deposit(self,amount):
        if amount < 2000:
            raise ValueError("Minimum deposit 2000")
        super().deposit(amount)

    def withdraw(self,amount):
        if amount > 5000:
            raise ValueError("withdraw limit 5000")
        super().withdraw(amount)





b = BankAccount("Ganesh",10000)

b1 = BankAccount("SURESH",6100)
b.transfer(b1,2000)

#print(b1.balance)





############################logger Inheritance########################

from csv import reader,writer
class ConsoleLogger:
    def log(self,message):
        print(message)


class TextFileLogger:

    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        self.file_object.write(message)
        self.file_object.write("\n")
        self.file_object.flush()


class CSVFileLogger:
    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        words = message.split()
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()




#
# file = open("demo2.csv","w",newline="")
#
# t = CSVFileLogger(file)
# t.log("hello welcome to python")
# t.log("hello welcome to python and java are OOPS languages")
# t.log("hello welcome OOPS")
# t.log("hello welcome dgs")
#





class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self,pattern):
        self.pattern = pattern

    def log(self,message):
        if self.pattern not in message:
            raise Exception(f"{self.pattern} not found ")
        super().log(message)


# p = FilteredConsoleLogger("error")
# p.log("the critical message")


class FilteredTextLogger(TextFileLogger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern not in message:
            raise Exception(f"{self.pattern} not in found")
        super().log(message)

file = open("demo3.txt","w")

# logger = FilteredTextLogger(file,"error")
# logger.log("this is a error message")
# logger.log("this is a error log")
# logger.log("this is a error batch")
# logger.log("this is a critical message")


class FilteredCSVLogger(CSVFileLogger):
    def __init__(self,file_object,pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self,message):
        if self.pattern in message:
            super().log(message)

# file_ = open("demo4.csv","w",newline="")
#
# logger = FilteredCSVLogger(file_,"error")
# logger.log("this is a error message")
# logger.log("this is a critical message")
# logger.log("this is a error text")
# logger.log("this is a bad text")



##############################composition Example###################################

class FilteredLogger:                   #duck typing(polymorphic behaviour)
    def __init__(self,pattern,logger_type):
        self.pattern = pattern
        self.logger_type = logger_type

    def log(self,message):
        if self.pattern in message:
            self.logger_type.log(message)

#-----ConsoleLogger--
# console_logger = ConsoleLogger()
# f_logger = FilteredLogger("error",console_logger)
# f_logger.log("this is an info message")


#-------TextFileLogger--------------
# f1 = open("demo.5.txt","w")
# textfile_logger = TextFileLogger(f1)
# f_logger = FilteredLogger("info",textfile_logger)
# f_logger.log("this is info message")
# f_logger.log("this is error message")
# f_logger.log("this is info log")
#


#--------CSVFileLogger-----------
# f1 = open("demo.6.csv", "w", newline="")
# csv_logger = CSVFileLogger(f1)
# f_logger = FilteredLogger("info", csv_logger)
# f_logger.log("this is an info message")
# f_logger.log("this is a error message")
# f_logger.log("this is a info log")




def filtered_logger(pattern):
    with open("sample.log","r") as fr, open("filtered.csv","w",newline="") as fw:
        logger = CSVFileLogger(fw)
        f_logger = FilteredLogger(pattern,logger)
        for line in fr:
            clean_line = line.strip()
            if clean_line:
                f_logger.log(line)

#filtered_logger("INFO")



##############################selenium version###################

import selenium

#print(selenium.__version__)


################################################################





######################## magic methods ####################


###container protocol

#__len__
#__contains__
#__getitem__
#__setitem__

class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __len__(self):
        return len(self.__dict__)

    def __contains__(self, item):
        if item in (self.__dict__.values()):
            return True
        return False

    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise IndexError("index out of range")


    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise IndexError("Index out of range")


class PositivePoint(Point):
    def __setitem__(self, index, value):
        if not isinstance(value,(int,float)):
            raise TypeError("invalid datatype")
        if value < 0:
            raise ValueError("Negative values not allowed")
        super().__setitem__(index,value)




class RangePoint(Point):
    def __setitem__(self, index, value):
        if index == 0:
            if 0 >= value or value > 50:
                raise ValueError("value should be within the range")
            else:
                super().__setitem__(index,value)
        elif index == 1:
             if 0 >= value or value > 100:
                 raise ValueError("value out of range")
             else:
                 super().__setitem__(index,value)

p = RangePoint(1,2)



##########################################################################################################


####Comaprison Protocol

#__lt__()
#__gt__()
#__eq__()
#__le__()
#__ge__()

class Employee:
    def __init__(self,name,age,pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __gt__(self, other):
        if self.age > other.age:
            return True
        return False

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return True

    def __eq__(self, other):
        if self.age == other.age:
            return True
        return False

###########################################################################################################






#################################################Atribute Protocol########################################


###__getattribute__
##__setattribute__


class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    # def __getattribute__(self, item):
    #     try:
    #         return super().__getattribute__(item)
    #     except AttributeError:
    #         return "attribute not found"

    def __getattribute__(self, item):
        return super().__getattribute__(item)


    def __setattr__(self, key, value):
        if value < 0:
            raise ValueError("invalid value")
        super().__setattr__(key,value)

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0


# p = Point(1,2)
# print(p.c)
# print(p.__dict__)



class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if not isinstance(value,(int,float)):
            raise TypeError("invalid type")
        super().__setattr__(key,value)

    def mul(self):
        return self.a * self.b

#c = Calculator("2",3)

#print(c.mul())

###############################################################################################################

#######################################Encapsulation##########################################################


class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("not valid")
        self._radius = value

    def circumference(self):
        try:
            return 2 * 3.143 * self.radius
        except TypeError:
            return "nothing"


# c = Circle(3)
# #print(c.circumference())
# c._radius = "gdgsd"
# print(c.__dict__)
# print(c.circumference())


#######################################################################################################



#######################################Abstraction###################################################

from abc import ABC,abstractmethod

@abstractmethod
class Logger:
    def log(self,message):
        pass


class FilteredConsoleLogger(Logger):
    def __init__(self,pattern):
        self.pattern = pattern

    def log(self,message):
        if self.pattern not in message:
            raise Exception(f"{self.pattern} not found ")
        super().log(message)


class FilteredTextLogger(Logger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self, message):
        if self.pattern not in message:
            raise Exception(f"{self.pattern} not in found")
        super().log(message)


class FilteredCSVLogger(Logger):
    def __init__(self,file_object,pattern):
        self.pattern = pattern
        super().__init__(file_object)

    def log(self,message):
        if self.pattern in message:
            super().log(message)

class Demo(Logger):
    def log(self,message):
        print("some message")



class FilteredLogger:                   #duck typing(polymorphic behaviour)
    def __init__(self,pattern,logger_type):
        self.pattern = pattern
        self.logger_type = logger_type

    def log(self,message):
        if self.pattern in message:
            self.logger_type.log(message)



d = Demo()

# f = FilteredLogger("info",d)
# f.log("this is error message")
#






sentence = "hello world welcome to python hello hi how are you hello there"
s = sentence.find("hello")
print(s)
n = 3
while s >= 0 and n > 1:
    s = sentence.find("hello",s + len(sentence))
    n -= 1
    # print(s)
    #



"""

from interview_programs import A


class B(A):

    def something(self):
        return self.some_method()
        super().some_method()

    # super().some_method()
print(B.__mro__)
b = B()
print(b.something())
"""












# def log(self,message):
#     with open("demo.txt","a") as file:
#         file.write(message)
#         file.write("\n")







































# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from re import findall,match

# driver = WebDriver()
# driver.get(r"C:/Users/GANESH%20S%20JOSHI/OneDrive/Desktop/demo-html/demo.html")
# driver.get("https://chatgpt.com/c/8c19a248-4051-4fed-bc68-117d6632a24b#7-conclusion")
# driver.maximize_window()
# current_url = driver.current_url
# pattern = r"https://chatgpt\.com/.+"
# if match(pattern,current_url):
#     print("pattren is present")
# else:
#     print("pattern is not present")

"""

driver.get("https://www.example.com/some-page")
# Get the current URL
current_url = driver.current_url

# Define a regular expression pattern
# pattern = r"https://www\.example\.com/.+"

# Use re.match() to check if the URL matches the pattern
if match(pattern, current_url):
    print("URL matches the pattern!")
else:
    print("URL does not match the pattern.")

driver.quit()
"""



"""# elements = driver.find_elements("xpath","//td[contains(text(),'Java')]//following-sibling::td//input[@type='checkbox']")
# driver.find_element("xpath","//td[text()='Android']//following-sibling::td[2]").click()
print(driver.find_element("xpath","//td[text()='Android']//following-sibling::td[2]").text)
sleep(5)
"""
# for i in elements:
#     print(i.click())

# div[class ~= 'puis-padding-right-micro'] > div:nth-child(2)> div > h2 >span



"""
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.maximize_window()
driver.get("https://www.amazon.in/s?i=fashion&rh=n%3A22371749031%2Cp_72%3A1318477031%2Cp_36%3A60000-%2Cp_n_feature_nineteen_browse-bin%3A11301363031&s=shoe&dc&fs=true&ds=v1%3Al8JPi25PB7TFRMjZXhBSVc0KA1Abkc1yMFs9s6HG8wc&_encoding=UTF8&content-id=amzn1.sym.956ad69b-6ad0-49d1-8316-edf3050e3342&pd_rd_r=52a1aae8-1515-432c-b06d-28786ca0f4d8&pd_rd_w=NrCNP&pd_rd_wg=fYCQF&pf_rd_p=956ad69b-6ad0-49d1-8316-edf3050e3342&pf_rd_r=MM5DRPHZCZ5HRSGTJWAH&qid=1713510673&rnid=11301362031&ref=pd_hp_d_btf_unk")
product_names =set([product.text for product in driver.find_elements("xpath",'//span[@class="a-size-base-plus a-color-base"]')])
# print(product_names)
d = {}
actual_price = []
for product_name in product_names:
    xpath_ = f"//div[contains(@class ,'puis-padding-right-micro')]//descendant::span[text()='{product_name}']//ancestor::div[contains(@class ,'puis-padding-right-micro')]//descendant::span[@class='a-price-whole']"
    prices =[int("".join(price.text.split(','))) for price in driver.find_elements("xpath",xpath_)]
    actual_price.append(prices)
for name,price_ in zip(product_names,actual_price):
    if name not in d:
        d[name] = price_
    else:
        d[name] += price_

print(d)
"""


#
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = WebDriver()
# driver.get("https://www.google.com")
# driver.maximize_window()
# search_box = driver.find_element("xpath","//textarea[@title='Search']")
# search_box.send_keys("Ganesh")
# search_box.send_keys(Keys.ENTER)
# sleep(15)
# elements = driver.find_elements("xpath","//*[contains(text(),'Ganesh')]")
# print(len(elements))




#
# //span[@class=max("post-count")]
#
# //book[not(number(@id) <= preceding-sibling::book/@id) and not(number(@id) <= following-sibling::book/@id)]
# //span[not(number(@class) <= preceding-sibling::span/@class) and not(number(@class) <= following-sibling::span/@class)]
#
# //section[@class="avatars"]//descendant::span

# driver.set_page_load_timeout(5)




expected_date = "2025-06-27"
formatted_date = datetime.strptime(expected_date,"%Y-%m-%d")
expected_year = formatted_date.year
expected_month = formatted_date.month
expected_day = formatted_date.day

print(type(expected_day))
print(type(expected_year))
print(type(expected_month))
