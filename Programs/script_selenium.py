#demo.py
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from csv import reader

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/books")
sleep(3)

#expected_prices = {
#            "Health Book": 10.00,
#            "Science": 51.00,
#            "Computing and Internet": 10.00,
#            "Copy of Computing and Internet EX": 10.00,
#            "Fiction": 24.00,
#            "Fiction EX": 24.00,
#            }


def read_data():
    prices = { }
    with open("/Users/sandeep/Desktop/training/_selenium/data_files/prices.csv") as f:
        rows = reader(f)
        headers = next(rows)        # skipping headers
        for row in rows:
            prices[row[0]] = float(row[1])
    return prices

expected_prices = read_data()

for product, expected_price in expected_prices.items():
    _xpath = f"//a[text()='{product}']/../..//span[@class='price actual-price']"
    # reading actual price from the application
    actual_price = driver.find_element("xpath", _xpath).text
    if expected_price == float(actual_price):
        print("PASS")
    else:
        print(f"FAIL: {product} expected price is {expected_price} and the actual is {actual_price}")




#books = ["Health Book", "Fiction"]
#
#for book in books:
#    driver.find_element("xpath", f"//a[text()='{book}']/../..//input[@value='Add to cart']").click()
#    sleep(3)









#driver.find_element("xpath", "//a[text()='Python 3.9.19']/../..//a[text()='Release Notes']").click()
# driver.find_element("xpath", "//td[text()='Ruby']/..//input[@name='download']").click()





























#element = driver.find_element("id", "multiple_cars")

#select = Select(element)
#
#select.select_by_visible_text("Audi")
#sleep(1)
#select.select_by_visible_text("Mercedes")
#sleep(1)
#select.select_by_visible_text("Toyota")
#sleep(1)
#select.select_by_index(4)






















#items = select.options
#
#_items = [ ]
## _items = [ item.text  for item in items ]
#for item in items:
#    _items.append(item.text)
#
#for item in _items[::-1]:
#    select.select_by_visible_text(item)
#    sleep(1)





































#select.select_by_visible_text("Audi")
#sleep(2)
#select.select_by_visible_text("Mercedes")
#sleep(2)
#
#select.select_by_index(10)
#sleep(2)
#
#select.select_by_value("min")
#sleep(2)
#select.select_by_value("for")




















#images = driver.find_elements("xpath", "//img")
#images_ = driver.find_elements(By.TAG_NAME, "img")
























#element = driver.find_element("name", "q")
#
#attributes = ["type", "class", "id", "autocomplete", "value", "name"]
#
#for attribute in attributes:
#    print(element.get_attribute(attribute))





















# links = driver.find_elements(By.XPATH, "//a")
#links = driver.find_elements(By.TAG_NAME, "a")
#
#data = [ ]
#
#for link in links:
#    link_text = link.text
#    href = link.get_attribute("href")
#    data.append((link_text, href))
#    sleep(0.1)



























#elements = driver.find_elements("xpath", "//input[@name='fname']")
## driver.find_elemetns("name", "fname")
#
#contents = ["apple", "google", "gmail", "yahoo", "flipkart", "facebook", "yelp", "amazon", "bestbuy"]
#
#
#for element, content in zip(elements, contents):
#    element.send_keys(content)
#    sleep(1)











#boxes = driver.find_elements("name", "download")



























# click on last checkbox
# boxes[-1].click()

# click on each check box in reversed order
#for box in boxes[::-1]:
#    box.click()
#    sleep(1)





























#driver.find_element("xpath", "//a[@class='ico-register']").click()
#sleep(1)
#
## //input[@id='gender-male']
## (//input[@name='Gender'])[1]
## (//input[@type='radio'])[1]
## //input[@value='M']
#driver.find_element("xpath", "//input[@id='gender-male']").click()
#sleep(1)
#
## //input[@id='FirstName']
## //input[@name='FirstName']
## (//input[@class='text-box single-line'])[1]
## (//input[@type='text'])[3]
#driver.find_element("xpath", "//input[@id='FirstName']").send_keys("hello")
#sleep(1)
#
#driver.find_element("xpath", "//input[@id='LastName']").send_keys("world")
#sleep(1)
#
#driver.find_element("xpath", "//input[@id='Email']").send_keys("hello.world@company.com")
#sleep(1)
#
#driver.find_element("xpath", "//input[@id='Password']").send_keys("Password123")
#sleep(1)
#
#driver.find_element("xpath", "//input[@id='ConfirmPassword']").send_keys("Password123")
#
#sleep(1)
#
#driver.find_element("xpath", "//input[@value='Register']").click()













#driver.find_element("xpath", "/html/body/div[1]/input[1]").send_keys("steve")
#sleep(1)
#driver.find_element("xpath", "/html/body/div[1]/input[2]").send_keys("Jobs")
#sleep(1)
#driver.find_element("xpath", "/html/body/div[2]/input[1]").send_keys("HP")
#sleep(1)
#driver.find_element("xpath", "/html/body/div[2]/input[2]").send_keys("Bangalore")
#sleep(1)


# Absolute xpath's
# /html/body/div[1]/input[1]    ---> Firstname
# /html/body/div[1]/input[2]   -----> LastName
# /html/body/div[2]/input[1]    ----> Company
# /html/body/div[2]/input[2]    -----> Location


























#driver.find_element("css selector", "a[class='ico-register']").click()
#sleep(1)


## input[id='gender-male']
## input[name='Gender']  ----> don't use
## input[type='radio'] -----> don't use
## input[value='M']
#driver.find_element("css selector", "input[id='gender-male']").click()
## driver.find_element("css selector", "input[value='M']").click()
#sleep(1)
#
## input[id='FirstName']
## input[name='FirstName']
#driver.find_element("css selector", "input[id='FirstName']").send_keys("hello")
#sleep(1)
#
#driver.find_element("css selector", "input[name='LastName']").send_keys("word")
#sleep(1)
#
#driver.find_element("css selector", "input[name='Email']").send_keys("hello.world@company.com")
#sleep(1)
#
# input[name='Password']
# input[id='Password']

#driver.find_element("css selector", "input[name='Password']").send_keys("Password123")
#sleep(1)
#
#driver.find_element("css selector", "input[id='ConfirmPassword']").send_keys("Password123")
#sleep(1)
#
## input[value='Register']
## input[id='register-button']
## input[name='register-button']
#
#driver.find_element("css selector", "input[value='Register']").click()
































# driver.find_element("partial link text", "Inbox").click()





























#driver.get("https://demowebshop.tricentis.com/")
#sleep(1)
#
## driver.find_element("class name", "ico-register").click()
#driver.find_element("link text", "Register").click()
#sleep(1)
#
#driver.find_element("id", "gender-male").click()
#sleep(1)
#
#driver.find_element("id", "FirstName").send_keys("hello")
#sleep(1)
#
#driver.find_element("name", "LastName").send_keys("world")
#sleep(1)
#
#driver.find_element("id", "Email").send_keys("hello.world@company.com")
#sleep(1)
#
#driver.find_element("id", "Password").send_keys("Password123")
#sleep(1)
#
#driver.find_element("id", "ConfirmPassword").send_keys("Password123")
#sleep(1)
#
#driver.find_element("id", "register-button").click()
#sleep(1)














