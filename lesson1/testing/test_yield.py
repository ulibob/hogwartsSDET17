import datetime

import pytest


@pytest.fixture(scope="module")
def login():
    print("登录操作")
    token=datetime.datetime.now()
    # yield token # yield 相当于return
    # print("登出操作")
    return token

def test_search():
    print("搜索")

def test_cart(login):
    print(login)
    print("购物")

# @pytest.mark.fixture()
def test_order(login):
    print(login)
    print("下单")