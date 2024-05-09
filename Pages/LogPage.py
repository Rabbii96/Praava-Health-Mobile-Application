from Pages.HomePage import HomePage
from Locators.locators import LogIn


class LogPage(HomePage):

    def __init__(self, driver):
        self.locator = LogIn
        self.driver = driver
        super(LogPage, self).__init__(driver)

    #LOGIN
    def loginuser(self):
        # self.driver.find_element(*self.locator.login_user_ID).clear()
        self.driver.find_element(*self.locator.loginuser_ID).send_keys("01852821994")

    def loginpass(self):
        # self.driver.find_element(*self.locator.login_pass_ID).clear()
        self.driver.find_element(*self.locator.loginpass_ID).send_keys("12345678")

    def login(self):
        self.driver.find_element(*self.locator.login_ID).click()