#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 被测类：计算器
def swarps():
    def inner(func):
        try:
            func()
        except Exception as E:
            print(E)
    return inner

class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def multiply(a, b):
        return a * b

    def subtract(a, b):
        return a - b
