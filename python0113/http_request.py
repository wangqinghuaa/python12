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


if __name__ == '__main__':
    # 登录
    loging_url = "http://localhost:8066/api/mgr/loginReq"
    login_data = {"username": "auto", "password": "sdfsdfsdf"}

    # 列出课程
    lists_url = "http://localhost:8066/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"

    res=Http_request().http_request(loging_url,login_data,"post")
    print("登录的结果是:{}".format(res.json()))

    list_res=Http_request().http_request(lists_url,{},"get",cookie=res.cookies)
    print("列出的课程是:{}".format(list_res.json()))