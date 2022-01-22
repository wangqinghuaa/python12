#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-08 20:54
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_06.1.py
# @Software : PyCharm


import requests
import pprint

class HttpRequests:
    '''利用request封装get，post请求    url：请求的地址
    data:传递的参数 非必填参数'''
#第一种写法
    # def http_requests(self,url,data,cookie=None):
    #     res=requests.post(url,data,cookies=cookie)
    #     return res #返回消息实体
    # def http_requests_01(self,url,cookie=None):
    #     res=requests.get(url,cookies=cookie)
    #     return res
#第二种写法：
    def http_requests(self,url,data,method,cookie=None):
        if method=="post":
            res=requests.post(url,data,method,cookies=cookie)
            return res
        else:
            res=requests.get(url,data,cookies=cookie)
            return res


if __name__ == '__main__':
#第一种写法
#登录
    # url = "http://localhost:8066/api/mgr/loginReq"
    # data = {"username": "auto", "password": "sdfsdfsdf"}
    # res=HttpRequests().http_requests(url,data)
    # print("登录的结果是：",res.json())

# 查询课程
#     url_1 = "http://localhost:8066/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
#     res_01=HttpRequests().http_requests_01(url_1,res.cookies)
#     pprint.pprint(res_01.json())
#     print(res_01.json()['retcode'])#字典取值
#     print(res_01.json()['retlist'][0]["id"])#字典取值
#     print(res_01.json()["retlist"][1]["name"])#字典取值

#第二种写法
# 登录
    url = "http://localhost:8066/api/mgr/loginReq"
    data = {"username": "auto", "password": "sdfsdfsdf"}
    res=HttpRequests().http_requests(url,data,"post")
    print("登录的结果是：{}".format(res.json()))
#查询课程
    url_1 = "http://localhost:8066/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"
    res_01=HttpRequests().http_requests(url_1,{},"get",res.cookies)
    print(res_01.json())
#获取返回的内容
    print(res.json()['retcode'])#字典取值
    print(res_01.json()["retlist"][0]["desc"])
    print(res_01.json()['retlist'][0]["id"])
    # print(res_01.json()["retlist"][1]["name"])