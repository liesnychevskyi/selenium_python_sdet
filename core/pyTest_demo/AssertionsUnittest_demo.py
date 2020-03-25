import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe")
        driver.get("http://www.google.com")
        title_page = driver.title
        print("Title is: ", title_page)
#  -------------------------------------------------------------------------------------------------//
        #  AssertEqual
        #  self.assertEqual("Google", title_page, "Page title is not same")
#  -------------------------------------------------------------------------------------------------//
        #  AssertNotEquals
        self.assertNotEqual("Google_9", title_page, "The same title")
#  -------------------------------------------------------------------------------------------------//


if __name__ == "__main__":
    unittest.main()

