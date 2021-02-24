import datetime

import pytest


# @pytest.fixture(scope="module")
@pytest.fixture(scope="session", autouse=True)
def login():
    print("雪球自己的登录操作")
    username="name" + str(datetime.datetime.now())
    yield username # yield 相当于return
    print("登出操作")