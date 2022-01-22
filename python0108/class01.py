#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-08 21:38
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class01.py
# @Software : PyCharm


class MathMethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def subtraction(self):
        return self.a-self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        return self.a/self.b