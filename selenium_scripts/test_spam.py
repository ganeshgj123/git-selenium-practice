class TestLogin:
    def test_login_positive(self, browser):
        print("executing test_spam")
        print(browser)

    def test_login_negative(self, browser):
        print("executing test_spam2")
        print(browser)

class TestRegistration:
    def test_register_male_user(self, browser):
        print("Registration of Male user")

    def test_register_female_user(self, browser):
        print("Registration of Female user")

    def test_register_duplicate_user(self, browser):
        print("Registration duplicate user")
