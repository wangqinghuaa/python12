#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 11:32
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_login.py
# @Software : PyCharm

from class_0109.http_request import Http_request
from ddt import ddt,data  #引入ddt
import unittest
from class_0109.get_data import GgtData
from python0109.do_excel import DoExcel

test_data=DoExcel("tests.xlsx","test").get_data()

@ddt
class Test_http(unittest.TestCase):

    @data(*test_data)
    def test_01_login_normal(self,item):
        res = Http_request().http_request(item['url'], eval(item['data']),item['method'],getattr(GgtData,"COOKIES"))
        if res.cookies:  #有cookies的话，就更新cookies
            setattr(GgtData,"COOKIES",res.cookies)

        print(res.json())
        try:
            self.assertEqual(item['expected'],res.json()["retcode"])
        except Exception as e:
            print("test_01_login_normal's error is:{}".format(e))
            raise e

if __name__ == '__main__':
    unittest.main()
