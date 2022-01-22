#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-08 21:37
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : math_method.py
# @Software : PyCharm


#接口测试的本质 就是测试类里面的函数
#单元测试的本质，测试函数 代码级别
#单元测试的框架  unitest+接口   pytest+web
#unitest+requests+htmlruner+jenkins
#pytest+selenium+jenkins+allure

#功能测试》》接口测试
#1. 写用例   TestCast
#2. 执行用例  1. TestSuite-存储用例   2. TestLoader-找用例，加载用例，储存到1的TestSuite
#3. 对比实际结果 判定是否通过--断言 Assert
#4. 出具体报告---TestTestRunner
#5.1.代码存放到jenkins上面--可以做定时执行 fail的接口可以通过邮箱发送到对应的人


import unittest
from python0108.class01 import MathMethod
#写一个测试类 对我们自己写的MathMethod模块里面的类进行测试

class TestMathMethod(unittest.TestCase):
    def test_add__one_1(self):
        res=MathMethod(1,1).add()
        print("1+1的结果是:{}".format(res))
        # 加一个断言，判断期望值和实际值比对结果，一致就通过，不一致就识别
        try:
            self.assertEqual(3, res,msg="两个1相加出错了") #期望值-结果值
        except Exception as e:
            print("出错啦！断言错误是{}".format(e))
            raise e

    def test_add__one_2(self):
        res=MathMethod(0,0).add()
        print("0+0的结果是:{}".format(res))
        try:
            self.assertEqual(0, res)
        except Exception as e:
            print("出错啦！断言错误是{}".format(e))
            raise e

    def test_add__one_3(self):
        res=MathMethod(-1,-2).add()
        print("-1+-2的结果是:{}".format(res))
        try:
            self.assertEqual(-3, res)
        except Exception as e:
            print("出错啦！断言错误是{}".format(e))
            raise e


class TestMathMethof(unittest.TestCase):
    def test_add__one_4(self):
        res=MathMethod(1,1).multiplication()
        print("1*1的结果是:{}".format(res))
        #加一个断言，判断期望值和实际值比对结果，一致就通过，不一致就识别
        try:
            self.assertEqual(1,res) #期望值-结果值
        except Exception as e:
            print("出错啦！断言错误是{}".format(e))
            raise e


    def test_add__one_5(self):
        res=MathMethod(0,0).multiplication()
        print("0*0的结果是:{}".format(res))
        try:
            self.assertEqual(0, res)
        except Exception as e:
            print("出错啦！断言错误是{}".format(e))
            raise e

    def test_add__one_6(self):
        res=MathMethod(-1,-2).multiplication()
        print("-1*-2的结果是:{}".format(res))
        try:
            self.assertEqual(2, res)
        except Exception as e:
            print("出错啦！断言错误是{}".format(e))
            raise e

if __name__ == '__main__':
    unittest.main()

