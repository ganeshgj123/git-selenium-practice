#test_registration.py
from lib1 import Selenium_Wrapper
from pytest import mark

headers = "gender, fname, lname, email, password"
data = [
        ("male", "steve", "jobs", "steve.jobs@company.com", "Password123"),
        ("female", "laura", "turner", "laura.turner@company.com", "Password123"),
        ]

@mark.parametrize(headers, data)
def test_registration(browser, gender, fname, lname, email, password):
    wrapper = Selenium_Wrapper(browser)

    wrapper.click_element(("link text", "Register"))

    if gender == "male":
        wrapper.click_element(("id", "gender-male"))
    else:
        wrapper.click_element(("id", "gender-female"))

    # Selenium_Wrapper.enter_text(wrapper, ("id", "FirstName"), value="hello")
    wrapper.enter_text(("id", "FirstName"), value=fname)

    wrapper.enter_text(("id", "LastName"), value=lname)

    wrapper.enter_text(("id", "Email"), value=email)

    wrapper.enter_text(("id", "Password"), value=password)

    wrapper.enter_text(("id", "ConfirmPassword"), value=password)

    wrapper.click_element(("id", "register-button"))
