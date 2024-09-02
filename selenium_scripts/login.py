#login.py
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import NoSuchElementException
from lib import Selenium_Wrapper

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")
sleep(4)

wrapper = Selenium_Wrapper(driver)

wrapper.click_element(("link text", "Log in"))
# click_element(driver, ("link text", "Log in"))
sleep(2)

wrapper.enter_text(("id", "Email"), value="bill.gates@company.com")
# enter_text(driver, ("id", "Email"), value="bill.gates@company.com")
sleep(1)

wrapper.enter_text(("id", "Password"), value="Password123")
# enter_text(driver, ("id", "Password"), value="Password123")
sleep(1)

wrapper.click_element(("xpath", "//input[@value='Log in']"))
# click_element(driver, ("xpath", "//input[@value='Log in']"))
sleep(1)

driver.close()

