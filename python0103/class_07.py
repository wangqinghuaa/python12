#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-16 8:42
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_07.py
# @Software : PyCharm


# s="hello"
# # print(s.find("p"))#寻找字符串里面的字符串
# #找到的话返回索引，找不到的话返回-1
#
# if s.find("9"):
#     new_s=s.replace("o","kevin")
# print(new_s)

import random
import time
# def gen_mobile():
#     phone="1"+random.choice(['3','5','6','7','8','9'])
#     for i in range(9):
#         num=random.randint(0,9)
#         phone+=str(num)
#     return phone
#
# res=gen_mobile()
# print(res)

# tel="数学课程"+str((int(time.time()*1000)))
# print(tel)

import logging
# logging.debug("method")
# logging.info("methods")
# logging.warning('123')
# logging.error('res')
# logging.critical('test')


#logger 收集日志  debug info error
#landdler 输出渠道：指定的文件，还是控制台


#定义一个日志收集器-不设置级别默认从warning开始收集
my_logger=logging.getLogger("python")

#设置级别
my_logger.setLevel("DEBUG")


#设置输出日志格式
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
#创建输出渠道
ch=logging.StreamHandler()
ch.setLevel("DEBUG")
ch.setFormatter(formatter)

fh=logging.FileHandler("py11.txt",encoding="utf-8")
fh.setLevel("DEBUG")
fh.setFormatter(formatter)

#两者对接-指定输出渠道
my_logger.addHandler(ch)
my_logger.addHandler(fh)


#收集日志
my_logger.debug("python自动化测试")
my_logger.error("python接口测试")
