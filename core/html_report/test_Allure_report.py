from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import allure
import pytest

allure.severity(allure.severity_level.NORMAL)
class TestOrangeHrm:

    allure.severity(allure.severity_level.MINOR)
    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        title_act = self.driver.title
        print(title_act)
        if title_act == "OrangeHRM":
            assert True
        else:
            assert False
        self.driver.quit()
        print("Test Completed..")

    allure.severity(allure.severity_level.BLOCKER)
    def test_logout(self):
        pytest.skip("Now I am skipping this test ...")

    allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        title_act = self.driver.title
        print(title_act)
        if title_act == "OrangeHRMD":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestFailScreenShot", attachment_type=
                          AttachmentType.PNG)
            self.driver.close()
            assert False
        print("Test Completed..")

# C:\Users\User\PycharmProjects\selenium_sdet\ pytest -v -s --alluredir="C:\Users\User\PycharmProjects\selenium_sdet\core\html_report\allure_repo" core\html_report\test_Allure_report.py
# allure serve C:\Users\User\PycharmProjects\selenium_sdet\core\html_report\allure_repo - generate allure report