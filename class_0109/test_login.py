#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 11:32
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_login.py
# @Software : PyCharm

from class_0109.http_request import Http_request
import unittest
from class_0109.get_data import GgtData

class Test_http(unittest.TestCase):

    def setUp(self):
        pass       #每个用例开始先执行
    def tearDown(self):
        pass       #每个用例结束后执行

    def __init__(self,methodName,url,data,method,expected):
        super(Test_http,self).__init__(methodName)
        self.url=url
        self.data=data
        self.method=method
        self.expected=expected

    def test_01_login_normal(self):
        res = Http_request().http_request(self.url, self.data,self.method,getattr(GgtData,"COOKIES"))
        if res.cookies:  #有cookies的话，就更新cookies
            setattr(GgtData,"COOKIES",res.cookies)

        print(res.json())
        try:
            self.assertEqual(self.expected,res.json()["retcode"])
        except Exception as e:
            print("test_01_login_normal's error is:{}".format(e))
            raise e

    # def test_02_login_normal(self):
    #     data_error = {"username": "auto", "password": ""}
    #     res = Http_request().http_request(self.url, data_error, "post")
    #     print("登录的结果是：{}".format(res.json()))
    #     try:
    #         self.assertEqual(1,res.json()["retcode"])
    #     except Exception as e:
    #         print("test_02_login_normal's error:{}".format(e))
    #         raise e
    #
    # def test_03_login_normal(self):
    #     add_data={'action': 'add_course','data': '''{"name":"初中数学","desc":"初中数学课程","display_idx":2}'''}
    #     res = Http_request().http_request(self.add_url, add_data, "post", getattr(GgtData,"COOKIES"))
    #     print("新建的课程是{}".format(res.json()))
    #     try:
    #         self.assertEqual(0,res.json()["retcode"])
    #     except Exception as e:
    #         print("test_03_login_normal's:{}".format(e))
    #         raise e
    #
    # def test_04_login_normal(self):
    #     add_data={'action': 'add_course',
    #                'data': '''{"name":"初中数学",
    #               "desc":"初中数学课程",
    #               "display_idx":2}'''}
    #     res = Http_request().http_request(self.add_url, add_data, "post", getattr(GgtData,"COOKIES"))
    #     print("新建的课程是{}".format(res.json()))
    #     try:
    #         self.assertEqual(1,res.json()["retcode"])
    #     except Exception as e:
    #         print("test_04_login_normal's error is:{}".format(e))
    #         raise e


if __name__ == '__main__':
    unittest.main()
