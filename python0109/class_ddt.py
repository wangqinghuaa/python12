#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 22:22
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_ddt.py
# @Software : PyCharm


#ddt结合unittest使用：来进行数据处理 第三方库
#装饰器 会在你的函数运行之前运行

from ddt import ddt,data,unpack
import unittest

test_data=[{"age":15,"name":"ermao"},{"age":15,"sex":"ermao"}] #相当于测试数据

@ddt()  #装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data,)#2个数据，执行两次用例
    def test_print_data(self,age):
        print("age",age)



