import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class LoginTest8(BasePage):
    def test_forgetpass_page(self):
        lp = LoginPage(self.driver)
        time.sleep(5)

        lp.forgetpass()
        time.sleep(2)

        lp.forgetusername("01727778083")
        time.sleep(2)

        lp.login1()


if __name__ == "__main__":
    unittest.main()