import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=0.5)
def test_rerun():
    # assert 1 == 1
    # assert 1 == 2
    # assert 2 == 3
    pytest.assume(1 == 4)
    pytest.assume(1 == 2)
    pytest.assume(1 == 1)
    pytest.assume(1 == 3)


