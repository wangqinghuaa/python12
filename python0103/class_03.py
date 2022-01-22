#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-06 20:59
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_03.py
# @Software : PyCharm




class Teacher:


    name="ermao"

    def functional_test(self):#实例方法
            print(self.name+"会敲代码")
    def automated_testing(self):#实例方法
            print("会唱歌")
    def the_performance_test(self):#实例方法
             print("会做蛋炒饭")
    @classmethod
    def swimming(cls): #类本身
        print(cls.name+"还要会游泳")  #会报错
    @staticmethod
    def sing(): #普通函数
        print(self.name+"要会唱歌")#会报错

tf=Teacher() #隐式传递
#类里面的方法分3种：
#实例方法：意味着这个方法 只能实例来调用(self.name+) 不创建实例会报错Teacher().functional_test()Teacher.automated_testing(tf)
#缺少一个位置参数self #显示传递-不建议使用
#类方法:@classmethodTeacher.swimming()tf.swimming()
# #静态方法：@staticmethodTeacher.swimming()tf.swimming()

