#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-13 20:52
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm



from python0113.http_request import Http_request
from python0113.do_excel import Do_Excel

class GetCookie:
    Cookie=None
# COOKIE=None
def run(test_data,sheet_name):
    for item in test_data:
        # global COOKIE
        print("正在测试的用例是：{0}".format(item["title"]))
        login_res=Http_request().http_request(item["url"],eval(item["data"]),item["method"],getattr(GetCookie,"Cookie"))
        if login_res.cookies:
            # COOKIE=login_res.cookies
            setattr(GetCookie,"Cookie",login_res.cookies)
        print("请求的结果是：{0}".format(login_res.json()))

        Do_Excel().write_back("testss.xlsx",sheet_name,item["case_id"]+1,str(login_res.json()))



test_data=Do_Excel().get_data("testss.xlsx","test")
run(test_data,"test")

