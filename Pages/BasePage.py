# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import os
import unittest
import HtmlTestRunner

# from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class BasePage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={"platformName": "Android",
                                  "appium:platformVersion": "9",
                                  "appium:deviceName": "Kibria",
                                  "appium:automationName": "UiAutomator2",
                                  "appium:app": "E:\\Appium\\PraavaAppium\\PraavaHealthAppium\\app\\Praava Health_1.19_Apkpure.apk"
                                  }
        )
        print("Test Started.......")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Complete")


# if __name__ == '__main__':
#     unittest.main(testRunner=HTMLTestRunner(output="E:\\Appium\\PraavaAppium\\PraavaHealthAppium\\reports"))