import pytest


@pytest.fixture(params=["harry", "hemin"])
def login(request):
    print("login")
    return request.param


def test_search(login):
    print(login)
    print("搜索")
