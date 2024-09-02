#demo.py
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from csv import reader
from selenium.common.exceptions import NoSuchElementException

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/books")
sleep(4)

# ---------------------------------------------------------------------
# StaleElementReferecence Exception
link = driver.find_element("xpath", "//a[text()='Register']")
print(link)
link.click()

sleep(3)

# refind the element with new element ID and click
link = driver.find_element("xpath", "//a[text()='Register']")
print(link)

link.click()
# ---------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Selecting date from date picker
# for _ in range(12):
while True:
    try:
        _xpath = "//h2[text()='June 2030']/../..//div[text()='26']"
        driver.find_element("xpath", _xpath).click()
        break
    except NoSuchElementException:
        driver.find_element("xpath", "//i[@class='fa fa-chevron-right']").click()
        sleep(1)
        continue
# ------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
# static table
cols = driver.find_elements("xpath", "//table[@name='customers']//td[3]")

actual_fnames = [ ]
for col in cols:
    actual_fnames.append(col.text)

sorted_fnames = sorted(actual_fnames)

if actual_fnames == sorted_fnames:
    print("Fname column in in sorted order")
else:
    print("Not sorted")
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# dynamic webtable
companies = ['MSFT', 'AA', 'AAPL', 'FB']

for company in companies:
    print(company, end="\t")
print()

while True:
    for company in companies:
        share_price = driver.find_element("xpath", f"//td[text()='{company}']/..//td[@class='price']").text
        print(share_price, end="\t")
        sleep(0.5)
    print()
# -------------------------------------------------------------------------------------

