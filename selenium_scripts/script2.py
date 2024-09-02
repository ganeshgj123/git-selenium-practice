from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach",True)

driver = WebDriver(options)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element("xpath","//span[text() = 'Login']").click()
driver.find_element("xpath","//input[@class='r4vIwl BV+Dqf']").send_keys("8861419524")
sleep(5)
element  = driver.find_element("xpath","//button[@class='QqFHMw twnTnD _7Pd1Fp']")
driver.execute_script("arguments[0].click();", element)




#//button[@class='QqFHMw twnTnD _7Pd1Fp']