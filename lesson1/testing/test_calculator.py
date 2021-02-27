# -*- coding:utf-8 -*-
import os
import sys,os
import allure
import pytest
import yaml

# from lesson1.pythoncode.Caculator import MyCalculator


# 添加 ./lesson1 到导包路径
# sys.path.append(r"C:\Users\ulibo\PycharmProjects\learning\hogwartsSDET17")
sys.path.append(os.path.join(os.getcwd(), "../.."))
# print(os.path.join(os.getcwd(), "../.."))
from lesson1.pythoncode.Caculator import MyCalculator

# print(sys.path)

# 加载数据的函数
def get_datas():
    with open("./datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


@pytest.fixture()
def get_instance():
    print("\n开始计算")
    calc = MyCalculator()
    yield calc
    print("\n结束计算")


@pytest.fixture(params=get_datas()["add"]["datas"])
def get_add_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas()["subtr"]["datas"])
def get_subtr_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas()["divid"]["datas"])
def get_divid_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas()["multi"]["datas"])
def get_multi_datas_with_fixture(request):
    return request.param


# 测试fixture参数化数据是否ok
def test_paramm(get_add_datas_with_fixture):
    print(get_add_datas_with_fixture)


# 测试类
@allure.feature("计算器")
class TestCalc:
    # 旧数据的获取，参数化
    # datas = get_datas()
    # add_data: dict = datas["add"]["datas"], datas["add"]["ids"]
    # subtr_data: dict = datas["subtr"]["datas"], datas["subtr"]["ids"]
    # multi_data: dict = datas["multi"]["datas"], datas["multi"]["ids"]
    # divid_data: dict = datas["divid"]["datas"], datas["divid"]["ids"]

    # 用fixture替换了setup、teardown功能
    # # 前置处理
    # # set_class只在类方法前，前置处理一次，与此类中的测试方法个数无关
    # def setup_class(self):
    #     # 计算器的实例化
    #     self.calc = MyCalculator()
    #     print("开始计算:\n")
    #
    # # 后置处理
    # # teardown_class只在类方法完后，后置处理一次，与此类中的测试方法个数无关
    # def teardown_class(self):
    #     print("计算结束.")

    # fixture参数化数据——调试用例

    # 用fixture传参数改造后的加法用例
    @allure.title("相加_{get_add_datas_with_fixture[0]} + {get_add_datas_with_fixture[1]}")
    @allure.story("相加功能")
    def test_add_fixture_data_test(self, get_instance, get_add_datas_with_fixture):
        f = get_add_datas_with_fixture
        # print(f[0],f[1],f[2])
        assert f[2] == get_instance.add(f[0], f[1])

    # 旧加法用例

    # @pytest.mark.parametrize("a, b, result", add_data[0], ids=add_data[1])
    # def test_add(self, get_instance, a, b, result):
    #     # print(a, b, result)
    #     assert result == get_instance.add(a, b)

    # 用fixture传参数改造后的减法测试用例
    @allure.title("相加_{get_subtr_datas_with_fixture[0]} + {get_subtr_datas_with_fixture[1]}")
    @allure.story("相减功能")
    def test_subtr_fixture_data_test(self, get_instance, get_subtr_datas_with_fixture):
        f = get_subtr_datas_with_fixture
        assert f[2] == get_instance.subtr(f[0], f[1])

    # 旧减法测试用例
    # @pytest.mark.parametrize("a, b, result", subtr_data[0], ids=subtr_data[1])
    # def test_subtr(self, get_instance, a, b, result):
    #     # print(a, b, result)
    #     assert result == get_instance.subtr(a, b)

    # 用fixture传参数改造后的乘法测试用例
    @allure.title("乘法_{get_multi_datas_with_fixture[0]} + {get_multi_datas_with_fixture[1]}")
    @allure.story("乘法功能")
    def test_multi_fixture_data_test(self, get_instance, get_multi_datas_with_fixture):
        f = get_multi_datas_with_fixture
        assert f[2] == get_instance.multi(f[0], f[1])

    # # 乘法测试用例
    # @pytest.mark.parametrize("a, b, result", multi_data[0], ids=multi_data[1])
    # def test_multi(self, get_instance, a, b, result):
    #     # print(a, b, result)
    #     assert result == get_instance.multi(a, b)


    # 用fixture传参数改造后的乘法测试用例
    @allure.title("除法_{get_divid_datas_with_fixture[0]} + {get_divid_datas_with_fixture[1]}")
    @allure.story("除法功能")
    def test_divid_fixture_data_test(self, get_instance, get_divid_datas_with_fixture):
        f = get_divid_datas_with_fixture
        assert f[2] == get_instance.divid(f[0], f[1])

    #
    # # 除法测试用例
    # @pytest.mark.parametrize("a, b, result", divid_data[0], ids=divid_data[1])
    # def test_divid(self, get_instance, a, b, result):
    #     # print(a, b, get_instance.divid(a, b), result)
    #     assert result == get_instance.divid(a, b)
