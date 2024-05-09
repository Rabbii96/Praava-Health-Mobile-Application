import unittest
import HtmlTestRunner
import random
from Pages.BasePage import BasePage

from Tests.BookAppoinmentTest import LoginTest1
from Tests.BookHealthCheckTest import LoginTest2
from Tests.ChangePassTest import LoginTest3
from Tests.EditProfileTest import LoginTest4
from Tests.ForgetUserNameTest import LoginTest5
from Tests.LinkServeContactTest import LoginTest6
from Tests.LoginWithEmailTest import LoginTest7
from Tests.LoginWithForgetPasswordTest import LoginTest8
from Tests.LoginWithSignupTest import LoginTest9
from Tests.LogoutTest import LoginTest10
from Tests.MapTest import LoginTest11
from Tests.MyAppointmentsTest import LoginTest12
from Tests.RegisterTest import LoginTest13
from Tests.SignupMembershipTest import LoginTest14
from Tests.SocialMediaTest import LoginTest15


Book_Appoinment = unittest.TestLoader().loadTestsFromTestCase(LoginTest1)
Book_Health = unittest.TestLoader().loadTestsFromTestCase(LoginTest2)
Change_Pass = unittest.TestLoader().loadTestsFromTestCase(LoginTest3)
Edit_Profile = unittest.TestLoader().loadTestsFromTestCase(LoginTest4)
Forget_Username = unittest.TestLoader().loadTestsFromTestCase(LoginTest5)
Link_Serve = unittest.TestLoader().loadTestsFromTestCase(LoginTest6)
Login_With_Email = unittest.TestLoader().loadTestsFromTestCase(LoginTest7)
Login_With_Forget_Pass = unittest.TestLoader().loadTestsFromTestCase(LoginTest8)
Login_With_Signup = unittest.TestLoader().loadTestsFromTestCase(LoginTest9)
Logout = unittest.TestLoader().loadTestsFromTestCase(LoginTest10)
Map = unittest.TestLoader().loadTestsFromTestCase(LoginTest11)
My_Appoinment = unittest.TestLoader().loadTestsFromTestCase(LoginTest12)
Register = unittest.TestLoader().loadTestsFromTestCase(LoginTest13)
Signup_Membership = unittest.TestLoader().loadTestsFromTestCase(LoginTest14)
Social_Media = unittest.TestLoader().loadTestsFromTestCase(LoginTest15)

SuitRun = unittest.TestSuite([Book_Appoinment, Book_Health, Change_Pass, Edit_Profile, Forget_Username, Link_Serve, Login_With_Email, Login_With_Forget_Pass, Login_With_Signup, Logout, Map, My_Appoinment, Register, Signup_Membership, Social_Media]) #htmlReport
# SuitRun = unittest.TestSuite([Book_Appoinment])
unittest.TextTestRunner(verbosity=2).run(SuitRun)

outfile = open("E:\\Appium\\PraavaAppium\\PraavaHealthAppium\\reports\\Report.html","w")
runner = HtmlTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description="This is Appium Framework"
)
runner.run(SuitRun)
