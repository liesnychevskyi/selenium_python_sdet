from selenium import webdriver
import unittest
import HtmlTestRunner
import time


class OrangeHrmTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "Web page Title is not matching")
        time.sleep(5)

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        self.assertEqual("OrangeHRM3", self.driver.title, "Web page Title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed..")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\report_HTML_files'))

# C:\Users\User\PycharmProjects\selenium_sdet\core\html_report>python test_OrangeHRM_login.py
# - command to run test for generate HTML report
