# -*- coding:utf-8 -*-
import pytest
import yaml
from lesson1.pythoncode.Caculator import MyCalculator


# 加载数据的函数
def get_datas():
    with open("./datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


# 测试类
class TestCalc:
    # 数据的获取
    datas = get_datas()
    add_data: dict = datas["add"]["datas"], datas["add"]["ids"]
    subtr_data: dict = datas["subtr"]["datas"], datas["subtr"]["ids"]
    multi_data: dict = datas["multi"]["datas"], datas["multi"]["ids"]
    divid_data: dict = datas["divid"]["datas"], datas["divid"]["ids"]

    # 前置处理
    # set_class只在类方法前，前置处理一次，与此类中的测试方法个数无关
    def setup_class(self):
        # 计算器的实例化
        self.calc = MyCalculator()
        print("开始计算:\n")

    # 后置处理
    # teardown_class只在类方法完后，后置处理一次，与此类中的测试方法个数无关
    def teardown_class(self):
        print("计算结束.")

    # 加法用例
    @pytest.mark.parametrize("a, b, result", add_data[0], ids=add_data[1])
    def test_add(self, a, b, result):
        # print(a, b, result)
        assert result == self.calc.add(a, b)

    # 减法测试用例
    @pytest.mark.parametrize("a, b, result", subtr_data[0], ids=subtr_data[1])
    def test_subtr(self, a, b, result):
        # print(a, b, result)
        assert result == self.calc.subtr(a, b)

    # 乘法测试用例
    @pytest.mark.parametrize("a, b, result", multi_data[0], ids=multi_data[1])
    def test_multi(self, a, b, result):
        # print(a, b, result)
        assert result == self.calc.multi(a, b)

    # 除法测试用例
    @pytest.mark.parametrize("a, b, result", divid_data[0], ids=divid_data[1])
    def test_divid(self, a, b, result):
        # print(a, b, result)
        assert result == self.calc.divid(a, b)
