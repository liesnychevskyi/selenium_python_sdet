import pytest


@pytest.yield_fixture()
def setup():
    print("Opening browser for signup")
    print("******* Once before every method ********")
    yield  # After statement (yield) is executed -> print("Once after every method") AfterMethod
    print("Closing browser after all actions")
    print("Once after every method")


def test_login_by_username(setup):
    print("This is Login by User Name")


def test_login_by_facebook(setup):
    print("This is Login by Facebook")


# C:\Users\User\PycharmProjects\selenium_sdet\core\all_tests>  - 1 option to run current test
# pytest -v -s C:\Users\User\PycharmProjects\selenium_sdet\core\all_tests\ - 2 option to run all package with tests
# C:\Users\User\PycharmProjects\selenium_sdet\core\all_tests>pytest -v -s Test_Login.py::test_login_by_facebook
