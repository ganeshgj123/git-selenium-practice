from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from pytest import Parser

allowed_browsers = ("chrome", "firefox", "safari", "edge")
execution_environments = ("test", "stage")

# this is called as Hook function
def pytest_addoption(parser):
    parser.addoption("--browser_name", dest="browser_name", action="store", default="chrome", choices=allowed_browsers)
    parser.addoption("--env", dest="env", action="store", default="test", choices=execution_environments)



#class TestConfigurations:
#    url = "https://demowebshop.tricentis.com/"
#    email = "steve.jobs@company.com"
#    password = "Password123"
#    # any other project releated or environment related stuff or configurations
#
#
#class StageConfigurations:
#    url = "https://demowebshop.tricentis.com/"
#    email = "hello.world@company.com"
#    password = "Password123"
#    # any other project releated or environment related stuff or configurations


@fixture
def project_config(request):
    class TestConfigurations:
        url = "https://demowebshop.tricentis.com/"
        email = "steve.jobs@company.com"
        password = "Password123"
        # any other project releated or environment related stuff or configurations

    class StageConfigurations:
        url = "https://demowebshop.tricentis.com/"
        email = "hello.world@company.com"
        password = "Password123"
        # any other project releated or environment related stuff or configurations

    environment = request.config.option.env

    if environment.lower() == "test":
        return TestConfigurations()
    elif environment.lower() == "stage":
        return StageConfigurations()


@fixture
def browser(request, project_config):
    # get the browser name from cmd line
    browser_class = request.config.option.browser_name
    print("*" * 50)
    print(f"\n executing tests in browser {browser_class}")

    if browser_class.lower() == "firefox":
        driver = Firefox()
    elif browser_class.lower() == "chrome":
        driver = Chrome()
    elif browser_class.lower() == "safari":
        driver = Safari()
    elif browser_class.lower() == "edge":
        driver = Edge()

    driver.maximize_window()
    print("*" * 50)
    print(f"\n Launching {request.config.option.env} URL")
    driver.get(project_config.url)
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
