from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver

@fixture()
def browser():
    print("Opening Browser")
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    print("Closing Browser")
    driver.close()


@fixture
def some_thing():
    class Employee:
        def __init__(self, fname, lname, pay):
            self.fname = fname
            self.lname = lname
            self.pay = pay
    e = Employee("steve", "jobs", 1000)
    return e

@fixture
def f1():
    return 10

@fixture
def f2():
    return "hello world"

@fixture
def f3():
    return [1, 2, 3]
