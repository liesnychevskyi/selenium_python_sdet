import pytest


@pytest.fixture()  # BeforeMethod executing once before every method
def setup():
    print("******* Once before every method ********")


def test_method_1(setup):
    print("This is test method 1")


def test_method_2(setup):
    print("This is test method 2")


