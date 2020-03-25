import unittest


# -------------------------------------------------------------------------------------//

def setUpMdule():  # Will be executed before all the module one time
    print("setUp module")


def tearDownMdule():  # Will be executed after all the module one time
    print("tearDown module")

# -------------------------------------------------------------------------------------//

class AppTesting(unittest.TestCase):

    @classmethod  # decorator
    def setUp(self):  # This method will be executed every time before each test method
        print("setUp")

    @classmethod
    def tearDown(self):  # This method will be executed every time after each test method
        print("teardown")

    @classmethod
    def setUpClass(cls):  # This method will be run just one time at the beginning of the Class
        print("one time at the beginning of this class")

    @classmethod
    def tearDownClass(cls):  # This method will be run just one time at the enf of this Class
        print("One time tear down")

    def test_search(self):
        print("This is search test")

    def test_advanced_search(self):
        print("This is advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid recharge")

    def test_postpaidRecharge(self):
        print("This is postal recharge")


if __name__ == "__main__":
    unittest.main()
