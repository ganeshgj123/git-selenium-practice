from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

#options.set_preference("dom.webnotifications.enabled", False) #--for firefox

options.add_argument("--disable-notifications")

options.add_experimental_option("detach",True)


driver = WebDriver(options=options)


driver.implicitly_wait(20)

driver.get(r"file:///C:/Users/GANESH%20S%20JOSHI/OneDrive/Desktop/demo-html/demo.html")

driver.maximize_window()

"""elements = driver.find_elements("xpath","//table[@name = 'companies']//input[@name='fname']")
words = ["sdssds","ndbhf","kdjfd","jfjdf","jdhjfdf","jfdd","hdfdf","jdfdd","fdfddf"]

for element,word in zip(elements,words):
    element.send_keys(word)

"""


#dynamic Xpath

companies = ["Android","Linux","Windows","iOS"]

"""
for company in companies:
    sleep(0.5)
    driver.find_element("xpath",f"//td[text() = '{company}']/..//td/.//a[text() = 'Download']").click()

"""
#######################################################################################################
"""brands = ["Apple","Google","Yahoo","Yelp"]

for brand in brands:
    sleep(1)
    driver.find_element("xpath",f"//td[text() = '{brand}']/..//td/.//a[text() = '{brand}']").click()

"""
##############################################################################################################



# element = driver.find_element("id","multiple_cars")
# select = Select(element)
# items = select.options
#
# for item in items[1:]:
#     sleep(0.5)
#     select.select_by_visible_text(f"{item.text}")
#
#
# for item in items[1:][::-1]:
#     sleep(0.5)
#     select.deselect_by_visible_text(f"{item.text}")
#
#######################################################################################################

#
# items = ["Perl","C++","Java","Swift","Python","C#","JavaScript"]
#
# for item in items:
#     sleep(1)
#     driver.find_element("xpath",f"//td[text() = '{item}']/..//td/.//input[@name='download']").click()

##############################################################################################################
#


# items1 = ["asas","dfsdf","erewr","frfre","bgffgb","fgfrtr","rrfr","mgbg","rdrw"]
# items2 = driver.find_elements("xpath", "//td/.//input[@name='fname']")
# print(items2)
# # for item1,item2 in zip(items1,items2):
# #     print(item1)
#

##############################################################################################################

#dynamic table
"""
names = ["AAPL","MSFT","AA","FB"]
volumes = [50,10,20,30]


for name in names:
    print(name, end="\t\t")
print()


while True:
    for name in names:
        price = driver.find_element("xpath", f"//td[text() = '{name}']/..//td[@class='price']").text
        sleep(0.5)
        print(price,end='\t')
    print()

"""

"""
for name in names:
    wb = WebDriverWait(driver, 20)
    v = EC.visibility_of_element_located(("class name", "price"))
    wb.until(v)
    # if wb.until(v):
    price = driver.find_element("xpath",f"//td[text() = '{name}']/..//td[@class='price']").text
    sleep(5)
    print(price)

"""


#############################################################################################################

#dynamic xpath

"""
for company in companies:
    sleep(0.5)
    driver.find_element("xpath",f"//td[text() = '{company}']/..//td/.//a[text() = 'Download']").click()

"""
########################################################################################################################
#confirmation alert

# driver.find_element("id","delete").click()
#
# obj = driver.switch_to.alert
#sleep(2)
#obj.accept()
#obj.dismiss()

######################################################################################
#simple alerts

"""driver.find_element("id","firstname").send_keys("hdhf")
driver.find_element("id","lastname").send_keys("jfdfd")
driver.find_element("id","submit").click()

obj1 = driver.switch_to.alert
sleep(3)
obj1.dismiss()

"""

################################################################################################################
#double click

element = driver.find_element("id","double-click")

action_obj = ActionChains(driver)
sleep(2)
action_obj.double_click(element).perform()

# t1 = driver.execute_script("return document.body.scrollHeight")
# print(t1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# newHeight = driver.execute_script("return document.body.scrollHeight")







###########################################################Redbus################################################
"""
driver.find_element("xpath","//span[text()='Account']").click()
sleep(5)
driver.find_element("xpath","//span[text() = 'Login/ Sign Up']").click()


frame_element = driver.find_element("xpath","//iframe[@class='modalIframe']")

driver.switch_to.frame(frame_element)
sleep(3)

#frame_source = index/name_attr/id_attr/web_element

element = driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
driver.switch_to.frame(element)

driver.find_element("xpath","//span[text() = 'Sign in with Google']").click()

#driver.switch_to.window("Sign In - Google Accounts")


handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
driver.find_element("id","identifierId").send_keys("gyaani1234@gmail.com")
driver.find_element("xpath","//span[text() = 'Next']").click()
"""


"""
driver.find_element("id","mobileNoInp").send_keys("8861419524")
sleep(2)


driver.find_element("xpath","//iframe[@title='reCAPTCHA']").click()

sleep(20)
#driver.switch_to.frame(frame_element_)


driver.find_element("xpath","//span[@class = 'f-w-b']").click()

sleep(20)

driver.switch_to.parent_frame()
# driver.switch_to_default_content()
frame_element1 = driver.find_element("xpath","//div[@class='modalContent']//iframe[@class='modalIframe']")

driver.switch_to.frame(frame_element1)
#//button[text() = 'VERIFY OTP']
sleep(5)
driver.find_element("xpath","//button[@id='verifyUser']").click()
sleep(5)
"""
############################################################################################################























