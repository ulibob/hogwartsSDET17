# -*- coding: utf-8 -*-

# 被测类：计算器（加减乘除）
class MyCalculator:
    def add(self, a, b):
        return a + b

    def subtr(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def divid(self, a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "除数不能为0"
