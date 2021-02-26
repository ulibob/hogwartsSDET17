import pytest
import time

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    time.sleep(3)
    assert False

@pytest.mark.dependency()
def test_b():
    time.sleep(3)
    pass

@pytest.mark.dependency(depends=["test_a"])
def test_c():
    time.sleep(3)

    # c 依赖 a，a失败则c不执行
    pass

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    time.sleep(3)

    pass

@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    time.sleep(3)

    # c跳过，e跳过
    pass