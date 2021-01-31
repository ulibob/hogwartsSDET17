# -*- coding: utf-8 -*-

# 被测类：计算器（加减乘除）

class MyCalculator:
    '''对输入数据首先进行校验是否为int、float
        此计算器不支持复数计算：complex
    '''
    def add(self, a, b):
        if isinstance((a), (float, int)) and isinstance((b), (float, int)):
            return a + b
        else:
            return "请输入数字"
    def subtr(self, a, b):
        if isinstance((a), (float, int)) and isinstance((b), (float, int)):

            return a - b
        else:
            return "请输入数字"
    def multi(self, a, b):
        if isinstance((a), (float, int)) and isinstance((b), (float, int)):
            return a * b
        else:
            return "请输入数字"
    def divid(self, a, b):
        if isinstance((a), (float, int)) and isinstance((b), (float, int)):
            try:
                result = a / b
                return result
            except ZeroDivisionError:
                return "除数不能为0"
        else:
            return "请输入数字"
