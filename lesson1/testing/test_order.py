import pytest


# @pytest.mark.run(order=2)
@pytest.mark.second
def test_foo():
    assert True


# @pytest.mark.run(order=1)
@pytest.mark.first
def test_bar():
    assert True
