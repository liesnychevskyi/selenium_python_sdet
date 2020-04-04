import pytest


@pytest.yield_fixture()
def setup():
    print("Open URL")
    print("******* Once before every method ********")
    yield  # After statement (yield) is executed -> print("Once after every method") AfterMethod
    print("Close the browser")
    print("Once after every method")


def test_signup_by_facebook(setup):
    print("This is Signup by Facebook")


def test_signup_by_g_mail(setup):
    print("This is Signup by G_mail")


# C:\Users\User\PycharmProjects\selenium_sdet\core\all_tests>  - 1 option to run current test

