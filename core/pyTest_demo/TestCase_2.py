import unittest
from selenium import webdriver
import time

class SearchEnginesTest(unittest.TestCase):

    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\selenium_sdet\\""drivers\\chromedriver.exe")
        self.driver.get("https://www.google.com")
        time.sleep(5)
        print(self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\selenium_sdet\\""drivers\\chromedriver.exe")
        self.driver.get("https://www.bing.com")
        time.sleep(5)
        print(self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
