import unittest

from core.test_cases_and_suites.Package_1.TC_LoginTest import LoginTest
from core.test_cases_and_suites.Package_1.TC_SignUpTest import SingUpTest
from core.test_cases_and_suites.Package_2.TC_PaymentTest import PaymentTest
from core.test_cases_and_suites.Package_2.TC_PaymentReturnTest import PaymentReturnTest

# Get all tests from packages

tc_login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc_sign_up = unittest.TestLoader().loadTestsFromTestCase(SingUpTest)
tc_payment = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc_payment_return = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)


# Creating test suite
sanity_tes_suite = unittest.TestSuite([tc_login, tc_sign_up])
unittest.TextTestRunner().run(sanity_tes_suite)


# functional_test_suite = unittest.TestSuite([tc_login, tc_sign_up])
# unittest.TextTestRunner().run(functional_test_suite)


# # Master test suite
master_test_suite = unittest.TestSuite([tc_login, tc_sign_up, tc_payment, tc_payment_return])
unittest.TextTestRunner(verbosity=2).run(master_test_suite)
