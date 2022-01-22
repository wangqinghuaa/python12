#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-11 22:22
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_while.py
# @Software : PyCharm


#
# count=0
#
# while count<10:
#     print("现在几点了")
#     count+=1
#     if count==10:
#         break


import requests
class HttpRequest:

    def __init__(self):
        pass


    def post_request(self):  # 类方法
        res = requests.post(url,data)
        global cookes
        cookes = res.cookies
        print("返回的结果是{}".format(res.json()))


    def get_request(self): #实例方法
        res=requests.get(url,data)
        print("返回的结果是{}".format(res.json()))



    @classmethod  #静态方法
    def add(cls):
        print(5+5)

    @staticmethod
    def print_msg():
        print("今天天气是真的很冷")

url="http://localhost:8066/api/mgr/loginReq"
data={"username":"auto","password":"sdfsdfsdf"}

res=HttpRequest().post_request()
HttpRequest().add()
HttpRequest().print_msg()



