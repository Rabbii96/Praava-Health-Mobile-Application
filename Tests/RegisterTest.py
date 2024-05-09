import time
import unittest
from Pages.BasePage import BasePage
from Pages.LogPage import LogPage
from Pages.HomePage import HomePage
from Pages.MiddlerightBarPage import middleRightBarPage  # class name of this page


class LoginTest13(BasePage):

    def test_MiddlerightBarPage(self):
        md = middleRightBarPage(self.driver)
        log = LogPage(self.driver)
        hm = HomePage(self.driver)
        time.sleep(5)

        log .loginuser()

        log .loginpass()

        log .login()


        md.register()
        time.sleep(3)
        md.reg_fstname("Kibria")
        time.sleep(3)
        hm.scroll_down1(689, 161)

        md.reg_middlename("Sarawar")
        time.sleep(3)
        md.reg_lastname("Sayem")
        time.sleep(3)
        md.dateofbirth()
        time.sleep(3)
        md.date_ok_ID()
        time.sleep(3)
        md.email_ID("kibriasarawar.qups@gmail.com")
        time.sleep(3)
        hm.scroll_down2(954, 297)

        md.selectgender()
        time.sleep(3)
        md.gendercancel()
        time.sleep(3)
        md.nationality("BANGLADESHI")
        time.sleep(3)
        md.selectstatus()
        time.sleep(3)
        md.statuscancel()
        time.sleep(3)
        hm.scroll_down3(1150, 394)

        md.selectoccupation()
        time.sleep(3)
        md.occupationcancel()
        time.sleep(3)
        hm.scroll_down3(1220, 450)
        md.phnnmbr("01852821994")
        time.sleep(3)
        md.address("Bakalia, Ctg")
        time.sleep(3)
        hm.scroll_down3(1300, 502)
        md.city("Chittagong")
        time.sleep(3)
        md.state("Chittagong")
        time.sleep(3)
        md.country("Bangladesh")
        time.sleep(3)
        md.postalcode("4000")
        time.sleep(3)
        hm.scroll_down4(1144, 544)

        md.emergncycontact("Sarawar")
        time.sleep(3)
        md.selectrelation()
        time.sleep(3)
        md.relationcancel()
        time.sleep(3)
        md.emergncycontact1("01727778083")
        time.sleep(3)
        hm.scroll_down5(1238, 626)

        md.aboutus()
        time.sleep(3)
        md.aboutuscancel()
        time.sleep(3)
        md.radioclick1_ID()
        time.sleep(3)
        md.radioclick2_ID()
        time.sleep(3)
        md.backtopreviouspage_XPATH()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()