import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time

sys.path.append("C://Users/User/PycharmProjects/selenium_sdet")  # adding project to the system environment
from POM_approach.pages.LoginPage import LoginPage  # import LoginPage


class LoginTest(unittest.TestCase):
    # -----------------------------------------------------------------------------// Variables
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="..\\drivers\chromedriver.exe")

    # -----------------------------------------------------------------------------// Set Up Class
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    # -----------------------------------------------------------------------------// Test
    def test_login(self):
        lp = LoginPage(self.driver)  # Object of LoginPage
        lp.set_user_name(self.username)
        lp.set_user_password(self.password)
        time.sleep(5)
        lp.click_login()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Title is not expected")

    # -----------------------------------------------------------------------------// Tear Down Class
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    # -----------------------------------------------------------------------------// Main runner and HTML report


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
       output= "C:\\Users\\User\\PycharmProjects\\selenium_sdet\\POM_approach\\report"))

    # -----------------------------------------------------------------------------// Run test from Command Prom
# python POM_approach/tests/LoginTest.py
