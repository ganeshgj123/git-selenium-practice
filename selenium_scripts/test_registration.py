#test_registration.py
from selenium.webdriver.chrome.webdriver import WebDriver
from lib1 import Selenium_Wrapper

def test_registration():
    driver = WebDriver()
    driver.get("https://demowebshop.tricentis.com/")

    wrapper = Selenium_Wrapper(driver)

    wrapper.click_element(("link text", "Register"))

    wrapper.click_element(("id", "gender-male"))

    # Selenium_Wrapper.enter_text(wrapper, ("id", "FirstName"), value="hello")
    wrapper.enter_text(("id", "FirstName"), value="hello")

    wrapper.enter_text(("id", "LastName"), value="world")

    wrapper.enter_text(("id", "Email"), value="hello.world@company.com")

    wrapper.enter_text(("id", "Password"), value="Password123")

    wrapper.enter_text(("id", "ConfirmPassword"), value="Password123")

    wrapper.click_element(("id", "register-button"))


def spam():
    print("Executing SPAM")


def greet():
    print("Executing Greet")













