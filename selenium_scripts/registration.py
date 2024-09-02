#registration.py
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from csv import reader
from selenium.common.exceptions import NoSuchElementException
from lib import Selenium_Wrapper

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")
sleep(4)

wrapper = Selenium_Wrapper(driver)

wrapper.click_element(("link text", "Register"))
sleep(2)

wrapper.click_element(("id", "gender-male"))
sleep(2)

wrapper.enter_text(("id", "FirstName"), value="hello")
sleep(2)

wrapper.enter_text(("id", "LastName"), value="world")
sleep(2)

wrapper.enter_text(("id", "Email"), value="hello.world@company.com")
sleep(2)

wrapper.enter_text(("id", "Password"), value="Password123")
sleep(2)

wrapper.enter_text(("id", "ConfirmPassword"), value="Password123")
sleep(2)

wrapper.click_element(("id", "register-button"))
sleep(1)

