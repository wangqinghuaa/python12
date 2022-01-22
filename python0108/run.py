#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-08 22:07
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm

import unittest
from python0108 import math_method
import HTMLTestRunnerNew


suite=unittest.TestSuite() #储存用例

#方法三 使用py文件执行-具体到模块名
load=unittest.TestLoader()
suite.addTest(load.loadTestsFromModule(math_method))

with open("test.report.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title="python单元测试报告",
                                            description="单元测试第一次报告",
                                            tester="xia")
    runner.run(suite)
# 备注：使用谷歌 火狐都可以打开
