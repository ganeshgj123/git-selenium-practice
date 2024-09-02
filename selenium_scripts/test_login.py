#test_login.py
from selenium.webdriver.chrome.webdriver import WebDriver
from lib1 import Selenium_Wrapper

def test_login():
    driver = WebDriver()
    driver.get("https://demowebshop.tricentis.com/")

    wrapper = Selenium_Wrapper(driver)

    wrapper.click_element(("link text", "Log in"))

    wrapper.enter_text(("id", "Email"), value="bill.gates@company.com")

    wrapper.enter_text(("id", "Password"), value="Password123")

    wrapper.click_element(("xpath", "//input[@value='Log in']"))

    driver.close()


def test_greeting():
    print("Executing Greeting")


