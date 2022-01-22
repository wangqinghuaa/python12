#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-08 20:30
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_06.py
# @Software : PyCharm


import requests

class HttpRequest:
    '''利用requests封装get请求和post请求
    method:请求方式 支持get  以及post 字符串形式的参数
    cookie:请求的时候传递cookie值'''

    def http_request(self,url,data,method,cookie=None):

        if method.lower()=="get":  #小写 unper(大写)
            res = requests.get(url, data, cookies=cookie)
        else:
            res = requests.post(url, data, cookies=cookie)
        return res #消息实体：包含响应头 状态码 响应报文 sessid cookis信息(响应结果的响应实体)


if __name__ == '__main__':
    #登录
    url = "http://localhost:8066/api/mgr/loginReq"
    data = {"username": "auto", "password": "sdfsdfsdf"}
    ses=HttpRequest().http_request(url,data,"post")
    print("登录的结果是{}".format(ses.json()))

    # 添加课程
    datas = "http://localhost:8066/api/mgr/sq_mgr/"
    payload = {'action': 'add_course','data': '''{"name":"初中数学",
              "desc":"初中数学课程",
              "display_idx":2}'''}
    ser=HttpRequest().http_request(datas,payload,"post",cookie=ses.cookies)
    print("新建的课程是{}".format(ser.json()))




