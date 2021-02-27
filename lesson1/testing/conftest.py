# conftest是固定的,不能改
import datetime
import os
import sys
from typing import List

import pytest

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))



# @pytest.fixture(scope="module")
@pytest.fixture(scope="session")
def login():
    print("登录操作》》》》》》")
    token = datetime.datetime.now()
    yield token  # yield 相当于return
    print("登出操作")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

        # if "add" in item._nodeid:
        #     item.add_marker(pytest.mark.add)
    # 将测试用例逆序
    items.reverse()