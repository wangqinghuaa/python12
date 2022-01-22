#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 14:03
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm


import unittest
from class_0109.test_login import Test_http
import HTMLTestRunnerNew

suite=unittest.TestSuite()


test_data = [{"url":"http://localhost:8066/api/mgr/loginReq",
              "data":{"username": "auto", "password": "sdfsdfsdf"},"expected":0,"method":"post"},
             {"url":"http://localhost:8066/api/mgr/loginReq",
              "data":{"username": "auto", "password": ""},"expected":1,"method":"post"},
             {"url": "http://localhost:8066/api/mgr/sq_mgr/",
              "data": {'action': 'add_course','data': '''{"name":"初中数学","desc":"初中数学课程","display_idx":2}'''},"expected":0,"method":"post"}]
for item in test_data:
    suite.addTest(Test_http("test_01_login_normal",item["url"],item["data"],item["method"],item["expected"]))
# load=unittest.TestLoader()
# suite.addTest(load.loadTestsFromTestCase(Test_http))

with open("test.report.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title="python单元测试报告",
                                            description="单元测试第一次报告",
                                            tester="xia")
    runner.run(suite)





