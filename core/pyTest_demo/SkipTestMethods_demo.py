import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest  # If you want to skip your test
    def test_search(self):
        print("Test 1")

    def test_advantagesearch(self):
        print("Test 2")

    def test_postpaidresearch(self):
        print("Test 3")

    @unittest.skip("I am skipping the test because it is needed")
    def test_searchsomething(self):
        print("Test 4")

    @unittest.skipIf(1 == 1, "Some message of reason")
    def test_login_by_google(self):
        print("Test 5")

    def test_login(self):
        print("Test 6")


if __name__ == "__main__":
    unittest.main()
