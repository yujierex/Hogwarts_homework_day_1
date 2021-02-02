#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator
datas_file = "./datas/calc.yml"

def get_datas(method):
    with open(datas_file) as f:
        datas = yaml.safe_load(f)
    return (datas[method]['datas'], datas[method]['ids'])


# yaml json excel csv xml
# 测试类
class TestCalc:
    add_datas: list = get_datas("add")
    div_datas: list = get_datas("div")
    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, result", add_datas[0], ids=add_datas[1])
    def test_add(self, a, b, result):
        print(f"a={a} , b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    # def test_add1(self):
        # datas = [[1, 1, 2], [100, 400, 300], [1, 0, 1]]
        # for data in datas:
        #     print(data)
        #     assert data[2] == self.calc.add(data[0], data[1])

    # 相除功能
    @pytest.mark.parametrize("a, b, result", div_datas[0], ids=div_datas[1])
    def test_div(self, a, b, result):
        if b == 0:
            print("除数不能为0")
            assert result == self.calc.div(a, b)
        elif a or b is not int:
            print("请输入数字")
            assert result == self.calc.div(a, b)
        else:
            print(f"a={a} , b ={b} ,result={result}")
            assert result == self.calc.div(a, b)