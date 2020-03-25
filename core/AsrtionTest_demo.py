import unittest
from selenium import webdriver


#  -------------------------------------------------------------------------------------------------//


class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe")
        driver.get("http://www.google.com")
        title_page = driver.title
        print("Title is: ", title_page)
        #  -------------------------------------------------------------------------------------------------//
        #  AssertTrue
        self.assertTrue(title_page == "Google")
        #  AssertFalse
        self.assertFalse(title_page == "Googleuuu")


#  -------------------------------------------------------------------------------------------------//

#  -------------------------------------------------------------------------------------------------//

if __name__ == "__main__":
    unittest.main()
