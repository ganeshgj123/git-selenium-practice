class Selenium_Wrapper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

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
