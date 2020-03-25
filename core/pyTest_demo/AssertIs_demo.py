import unittest
from selenium import webdriver


#  -------------------------------------------------------------------------------------------------//


class Test(unittest.TestCase):

    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe")
        # It will verify is variable is null or not (If variable is contents some value it returns False)
        # driver = None
        # self.assertIsNone(driver)
        self.assertIsNotNone(driver)

        driver.get("http://www.google.com")
        title_page = driver.title
        print("Title is: ", title_page)
        #  -------------------------------------------------------------------------------------------------//
        #  AssertIsNone
        #  self
        #  AssertNotNone
        #  self


#  -------------------------------------------------------------------------------------------------//

#  -------------------------------------------------------------------------------------------------//



if __name__ == "__main__":
    unittest.main()