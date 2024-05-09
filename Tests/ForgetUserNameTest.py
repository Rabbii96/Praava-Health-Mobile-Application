import time

from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage



class LoginTest5(BasePage):
    def test_forgetusername_page(self):
        lp = LoginPage(self.driver)
        time.sleep(5)

        lp.forgetusern()
        time.sleep(2)

        lp.forgetusermob("Kibria Sarawar Sayem")
        time.sleep(2)

        lp.login2()


if __name__ == "__main__":
    unittest.main()