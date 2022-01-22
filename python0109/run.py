#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 14:03
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm


import unittest
from python0109.test_login import Test_http
import HTMLTestRunnerNew


suite=unittest.TestSuite()

load=unittest.TestLoader()
suite.addTest(load.loadTestsFromTestCase(Test_http))

with open("test.report.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title="python单元测试报告",
                                            description="单元测试第一次报告",
                                            tester="xia")
    runner.run(suite)





