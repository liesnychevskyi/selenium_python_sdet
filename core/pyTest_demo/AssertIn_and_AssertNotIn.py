import unittest
from selenium import webdriver


#  -------------------------------------------------------------------------------------------------//


class Test(unittest.TestCase):

    def testName(self):
        list = ("Python", "Selenium", "TestNg", "QA")
        # self.assertIn("Python", list)  # It is looking value in the list
        self.assertNotIn("QA", list)


#  -------------------------------------------------------------------------------------------------//

#  -------------------------------------------------------------------------------------------------//


if __name__ == "__main__":
    unittest.main()
