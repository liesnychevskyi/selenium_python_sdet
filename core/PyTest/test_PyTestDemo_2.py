import pytest


@pytest.yield_fixture()
def setup():
    print("******* Once before every method ********")
    yield  # After statement (yield) is executed -> print("Once after every method") AfterMethod
    print("Once after every method")


def test_method_3(setup):
    print("This is test method 3")


def test_method_4(setup):
    print("This is test method 4")
