import pytest

@pytest.mark.login
def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a is not eq to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

@pytest.mark.login
def test_m3():
    assert True


@pytest.mark.login
def test_m4():
    assert False

@pytest.mark.login
def test_m5():
    assert 100 == 100

def test_m6():
    assert "jaspreet" == "JASPREET"

@pytest.mark.home
def my_test_m7():
    assert  False, "bad function name"
