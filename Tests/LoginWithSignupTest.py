import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage

class LoginTest9(BasePage):
    def test_signup_page(self):
        lp = LoginPage(self.driver)
        time.sleep(5)

        lp.click_signup()
        time.sleep(2)

        lp.mobile("01852821994")
        time.sleep(2)

        lp.username("Kibria")
        time.sleep(2)

        lp.password("12345678")
        time.sleep(2)

        lp.repassword("12345678")

        lp.email("kibriasarawar.qups@gmail.com")

        lp.login0()


if __name__ == "__main__":
    unittest.main()