#test_login.py
from lib1 import Selenium_Wrapper
from pytest import mark

headers = "username, password"

data = [
        ("bill.gates@company.com", "Password123"),
        ("hello.world@company.com", "Password123")
        ]

@mark.parametrize(headers, data)
def test_login(browser, username, password):
    wrapper = Selenium_Wrapper(browser)

    wrapper.click_element(("link text", "Log in"))

    wrapper.enter_text(("id", "Email"), value=username)

    wrapper.enter_text(("id", "Password"), value=password)

    wrapper.click_element(("xpath", "//input[@value='Log in']"))
