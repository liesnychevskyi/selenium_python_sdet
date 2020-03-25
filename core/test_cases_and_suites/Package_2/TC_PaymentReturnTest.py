import unittest


class PaymentReturnTest(unittest.TestCase):

    def test_paymentReturnByBank(self):
        print("This is Payment return by Bank")
        self.assertTrue(True)

    def test_paymentReturnBySeller(self):
        print("This is Payment by seller")
        self.assertTrue(True)

    def test_paymentReturnByThirdPart(self):
        print("This is Payment return by Someone")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
