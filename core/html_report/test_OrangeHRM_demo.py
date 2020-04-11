from selenium import webdriver
import pytest
import time


class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=
                                       "C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"
        time.sleep(5)

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        assert self.driver.title == "OrangeHRMh"

# pytest -v -s --html=report.html --self-contained-html test_(test name)
# pytest -v -s --html=report.html --self-contained-html test_OrangeHRM_demo.py
# pytest -v -s --html=.\report_HTML_files\report.html --self-contained-html test_OrangeHRM_demo.py