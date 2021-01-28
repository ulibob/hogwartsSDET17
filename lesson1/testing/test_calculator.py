# -*- coding:utf-8 -*-
import os

import pytest
import yaml
from lesson1.pythoncode.Caculator import MyCalculator


# 加载数据的函数
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas["add"]["datas"], datas["add"]["ids"]


# 测试类
class TestCalc:
    # 数据的获取
    data:list = get_datas()

    # 前置处理
    def setup_class(self):
        print("开始计算:\n")
        # 计算器的实例化
        self.calc = MyCalculator()

    # 后置处理
    def teardown_class(self):
        print("计算结束.")

    # 加法用例
    @pytest.mark.parametrize("a, b, result", data[0], ids=data[1])
    def test_add(self, a, b, result):
        print(a, b, result)
        assert result == self.calc.add(a, b)

    # todo 完善加法测试用例
    # todo 编写除法测试用例
    # 除法用例
