# -*- coding: utf-8 -*-

# 被测类：计算器（加法、除法）
class MyCalculator:
    def add(self, a, b):
        return a + b

    def divid(self, a, b):
        return a / b
        # try:
        # return a / b
        # except ZeroDivisionError:
        # return "除数不能为0"
