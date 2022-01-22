#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 11:23
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : http_request.py
# @Software : PyCharm


import requests

class Http_request:


    def http_request(self,url,data,method,cookie=None):
        try:
            if method.lower()=='get':
                res = requests.get(url,data,cookies=cookie)
            #艾已付
            elif method.lower()=='post':
                res = requests.post(url, data, cookies=cookie)
            elif method.lower()=='delete':
                res = requests.delete(url, cookies=cookie)
            elif method.lower()=='put':
                res = requests.put(url, data, cookies=cookie)
            #艾欧斯
            else:
                print("请求参数错误")
            return res
        #一颗赛普特  一颗赛普深
        except Exception as e:
            print("请求报错了：{}".format(e))
            raise e  #瑞z
