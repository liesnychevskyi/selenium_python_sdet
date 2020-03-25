import unittest
from selenium import webdriver


#  -------------------------------------------------------------------------------------------------//


class Test(unittest.TestCase):

    def testName(self):
        #  AssertGrate
        #  self.assertGreater(100, 1)
        #  self.assertGreater(1, 100)
        #  -------------------------------------------------------------------------------------------------//
        #  AssertGrateEqual (100, 100), (101, 100)  wil pass
        #  self.assertGreaterEqual(100, 101)  # (100, 101) wil not pass
        #  -------------------------------------------------------------------------------------------------//
        #  AssertLess
        self.assertLess(100, 101)
        #  -------------------------------------------------------------------------------------------------//
        #  AssertLessEqual
        self.assertLessEqual(100, 100)


if __name__ == "__main__":
    unittest.main()
