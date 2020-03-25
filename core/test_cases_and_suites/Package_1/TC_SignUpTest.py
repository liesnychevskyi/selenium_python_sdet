import unittest


class SingUpTest(unittest.TestCase):

    def test_SignUpByEmail(self):
        print("This is Sign by Email")
        self.assertTrue(True)

    def test_SignByFacebook(self):
        print("This is Sign by Facebook")
        self.assertTrue(True)

    def test_SignUpByTwitter(self):
        print("This is Sign by Twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
