from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.chrome.webdriver import WebDriver

def _wait(func):
    def wrapper(*args, **kwargs):# (self, ("id", "FirstName")) {"value": "hello"}
        # create an obj instance for WebDriverWait class
        instance = args[0]
        locator = args[1]
        print(f"Waiting for element {locator}")
        wait = WebDriverWait(instance.driver, 10)    # self.driver
        v = visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper


def wait(cls):
    for key, value in cls.__dict__.items():
        if callable(value) and key != "__init__":
            setattr(cls, key, _wait(value))
    return cls
    

@wait      # Selenium_Wrapper = wait(Selenium_Wrapper)
class Selenium_Wrapper:
    def __init__(self, driver):
        self.driver = driver

#    def __setattr__(self, name, value):
#        if name == "driver":
#            if not isinstance(value, WebDriver):
#                raise TypeError("WebDriver instance expected")
#        super().__setattr__(name, value)


#    @property
#    def driver(self):
#        return self._driver
#
#    @driver.setter
#    def driver(self, value):
#        if not isinstance(value, WebDriver):
#            raise TypeError("WebDriver instance expected")
#        self._driver = value
    
    #@_wait      # click_element = _wait(click_element)
    def click_element(self, locator):
        self.driver.find_element(*locator).click()  # find_element("id", "FirstName")

    #@_wait      # enter_text = _wait(enter_text)
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    #@_wait      # select_item = _wait(select_item)
    def select_item(self, locator, *, item):
        list_box = self.driver.find_element(*locator)
        select = Select(list_box)
        select.select_by_visible_text(item)

# Not a good idea
#def click_element(driver, locator):
#    driver.find_element(*locator).click()
#
#def enter_text(driver, locator, value):
#    driver.find_element(*locator).send_keys(value)
