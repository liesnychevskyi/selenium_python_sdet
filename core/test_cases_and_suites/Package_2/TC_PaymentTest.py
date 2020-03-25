import unittest


class PaymentTest(unittest.TestCase):

    def test_paymentInDollar(self):
        print("This is Payment in Dollar")
        self.assertTrue(True)

    def test_paymentInEuro(self):
        print("This is Payment in Euro")
        self.assertTrue(True)

    def test_paymentInPound(self):
        print("This is Payment in Pound")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
