from datetime import datetime
from time import sleep

from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# driver = WebDriver()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
"""#dropdowns handling"""

# dropdown = driver.find_element("id","drop1")
# select = Select(dropdown)
# # select.select_by_visible_text("doc 1")
# sleep(2)
# select.select_by_index(2)
# sleep(2)
# select.select_by_value("jkl")
# sleep(2)

# options = select.options
# # select.select_by_visible_text(options[-1].text)
# sleep(2)

# for item in options[::-1]:
#    select.select_by_visible_text(item.text)
#    sleep(1)

# dd = driver.find_element("xpath",'//select[@id="multiselect1"]')
# select = Select(dd)
# opts = [option.text for option in select.options]
# for item in opts:
#     select.select_by_visible_text(item)
#     sleep(1)
# for item in opts[::-1]:
#     select.deselect_by_visible_text(item)
#     sleep(1)
#
#
# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
# driver = WebDriver(options=chrome_options)
# driver.maximize_window()
# driver.get("https://www.hdfcbank.com/")
# # # element = driver.find_element("xpath",'//div[@class="drp1"]//descendant::span[text()="Select Product Type"]')
# #
# element = WebDriverWait(driver,15).until(expected_conditions.visibility_of_element_located(("xpath",'//div[@class="drp1"]//descendant::span[text()="Select Product Type"]')))
# element.click()
# # #1
# options = driver.find_elements("xpath",'//div[@class="drp1"]//descendant::li')
# for i in options:
#     print(i.text)





########################################iframes################################
"""
driver = WebDriver()
driver.switch_to.frame("fed")
driver.switch_to.parent_frame()
driver.switch_to.default_content()

"""

##################handling infobar###########################
"""
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension",False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = WebDriver(options=chrome_options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
sleep(3)
"""



#######################handling mouse events#######################

#####hovering on an element#########################
"""
driver = WebDriver()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

action = ActionChains(driver)
"""


################hovering and clicking on an element##################
"""
element = driver.find_element("xpath",'//span[@id="blogsmenu"]')
action.move_to_element(element).perform()
sleep(2)
element2 = driver.find_element("xpath",'//span[text()="Selenium143"]')
#1st method
# action.move_to_element(element2).click().perform()
#2nd method
action.click(element2).perform()

sleep(2)

"""

###############slider-handling##################

"""driver = WebDriver()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
"""
"""element = driver.find_element("css selector" , "a[aria-labelledby = 'price-min-label']")
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(element,100,0).perform()
"""

#########right click mouse event################
"""
driver = WebDriver()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

element = driver.find_element("name","search")
actions = ActionChains(driver)
actions.context_click(element).perform()
sleep(3)

"""


#############drag and drop an element using click and hold#################
"""
driver = WebDriver()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actions = ActionChains(driver)
element1 = driver.find_element("id","box1")
element2 = driver.find_element("id","box106")
actions.drag_and_drop(element1,element2).perform()
sleep(3)
# actions.click_and_hold(element1).move_to_element(element2).release().perform()
# sleep(3)
"""


################### Keys events #################################

"""
driver = WebDriver()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

actions = ActionChains(driver)

elements = driver.find_elements("xpath",'//div[@id="LinkList1"]//a')

for element in elements:
    actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
sleep(5)

"""


####################### JavaScript  execution ######################


####find the height of the webpage
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

total_height = driver.execute_script("return document.body.scrollHeight")

print(f"Total height of the page: {total_height} pixels")
"""



######################headless mode execution################

#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = WebDriver(options=chrome_options)
#
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/")
#
# width = 1920
# height = driver.execute_script("return Math.max(document.body.scrollHeight,document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight);")
# driver.set_window_size(width,height)
# driver.find_element("tag name","body")
# driver.save_screenshot(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs\s1.png")
#
#


####### running the browser in maximized mode#########

"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(options=chrome_options)
driver.get("https://omayo.blogspot.com/")

sleep(3)
"""

######## opening the browser in full screen mode

"""
chrome_options = Options()
chrome_options.add_argument("--kiosk")
driver = WebDriver(options=chrome_options)
driver.get("https://omayo.blogspot.com/")

sleep(3)"""





#############################################################################################
############## Window handling ####################################

##########handling multiple windows at the same time###############
"""
driver = WebDriver()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
print(driver.title)

sleep(3)
driver.switch_to.new_window("tab")
driver.switch_to.new_window("window")
driver.get("https://selenium143.blogspot.com/")
print(driver.title)
sleep(3)


"""




########################################## Dynamic xpath ##############
"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://omayo.blogspot.com/")

links = driver.find_elements("xpath",'//div[@class="widget LinkList"]//descendant::a')
# print([link.text for link in links])
link_texts = [link.text for link in links]


for link_text in link_texts:
    xpath_ = f"//div[@class='widget LinkList']//descendant::a[text() = '{link_text}']"
    driver.find_element("xpath",xpath_).click()
    sleep(2)
    driver.back()


for link_text in link_texts:
    text_ = f"{link_text}"
    driver.find_element("link text",text_).click()
    sleep(2)
    driver.back()
"""


######################## calender handling type 1########################
"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element("id","datepicker").click()

element = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(("id","ui-datepicker-div")))
"""
##### generic way
"""
current_month = driver.find_element("class name","ui-datepicker-month").text
current_year = driver.find_element("class name","ui-datepicker-year").text

while not(current_year == "2025" and current_month == "June"):
    driver.find_element("xpath","//span[text()='Next']").click()
    current_month = driver.find_element("class name", "ui-datepicker-month").text
    current_year = driver.find_element("class name", "ui-datepicker-year").text
driver.find_element("xpath","//a[text()='24']").click()
sleep(5)
"""

#### date picker dynamic path

"""
def select_date(day,month,year):
    current_month = driver.find_element("class name", "ui-datepicker-month").text
    current_year = driver.find_element("class name", "ui-datepicker-year").text

    while not (current_year == year and current_month == month):
        driver.find_element("xpath", "//span[text()='Next']").click()
        current_month = driver.find_element("class name", "ui-datepicker-month").text
        current_year = driver.find_element("class name", "ui-datepicker-year").text
    xpath_ = f"//a[text()={day}]"
    driver.find_element("xpath", "//a[text()='24']").click()
    sleep(5)

select_date("26","October","2025")

"""

##############using javascript####################
"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.execute_script("document.getElementById.('datepicker').value = '25/08/2025'")
sleep(5)
"""


##############calender date for future and present #####################

"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")


expected_date = "2025-06-27"
formatted_date = datetime.strptime(expected_date,"%Y-%m-%d")
expected_year = formatted_date.year
expected_month = formatted_date.month
expected_day = formatted_date.day


driver.find_element("id","datepicker").click()

wait = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(("id","ui-datepicker-div")))

month_text = driver.find_element("class name",'ui-datepicker-month').text
month_dict = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
month_number = month_dict[month_text]
year_text = driver.find_element("class name",'ui-datepicker-year').text
year_number = int(year_text)


while not(expected_month > month_number or expected_year > year_number):
    driver.find_element("xpath","//span[text()='Next']").click()

    month_text = driver.find_element("class name", 'ui-datepicker-month').text
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                  "September": 9, "October": 10, "November": 11, "December": 12}
    month_number = month_dict[month_text]
    year_text = driver.find_element("class name", 'ui-datepicker-year').text
    year_number = int(year_text)

xpath_ = f"//a[text()='{expected_day}']"
driver.find_element("xpath",xpath_)
sleep(5)


while not(expected_month < month_number or expected_year < year_number):
    driver.find_element("xpath","//span[text()='Prev']").click()

    month_text = driver.find_element("class name", 'ui-datepicker-month').text
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                  "September": 9, "October": 10, "November": 11, "December": 12}
    month_number = month_dict[month_text]
    year_text = driver.find_element("class name", 'ui-datepicker-year').text
    year_number = int(year_text)

xpath_ = f"//a[text()='{expected_day}']"
driver.find_element("xpath",xpath_)
sleep(5)"""




#### entering text into field 3 calender  #############
"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://demo.guru99.com/test/")

driver.find_element("name","bdaytime").send_keys("20062024")
driver.find_element("name","bdaytime").send_keys(Keys.TAB)
driver.find_element("name","bdaytime").send_keys("1020")
driver.find_element("name","bdaytime").submit()
sleep(5)
"""



################type 4 calender dropdown ###################





######################type5 --  calender that consists of past and future dates in the same box
"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

wait = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(("css selector","div[id*= 'datepicker']")))

driver.find_element("id","fourth_date_picker").click()

month = driver.find_element("class name","ui-datepicker-month")
year = driver.find_element("class name","ui-datepicker-year")

select_month = Select(month)
select_year = Select(year)

select_month.select_by_visible_text("Jun")
select_year.select_by_visible_text("2025")

driver.find_element("xpath",'//td[not(contains(@class," ui-datepicker-other-month "))]/a[text()="25"]').click()
sleep(5)

# date   ---- //td[not(contains(@class," ui-datepicker-other-month "))]/a[text()='25']
"""



#########################type 6 click on the calender icon


# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# driver = WebDriver(chrome_options)
# driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
# sleep(5)
#
# wait = WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(("id","ui-datepicker-div")))




##################################### fetching the table data ######################
"""
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = WebDriver(chrome_options)
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")

headers = [i.text for i in driver.find_elements("xpath",'//table[@id="customers"]//tr[1]//span')]
print("    ".join(headers))

for i in range(2,7):
    xpath_ = f'//table[@id="customers"]//tr[{i}]//span'
    data = driver.find_elements("xpath", xpath_)
    print("    ".join([i.text for i in data]))

"""




