#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-09 13:59
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm








import unittest
from python0108 import math_method
import HTMLTestRunnerNew


suite=unittest.TestSuite() #储存用例

#方法二 通过类加载用例
load=unittest.TestLoader()
suite.addTest(load.loadTestsFromModule(math_method))

with open("test.report.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title="python单元测试报告",
                                            description="单元测试第一次报告",
                                            tester="xia")
    runner.run(suite)
# 备注：使用谷歌 火狐都可以打开
