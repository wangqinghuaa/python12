#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-31 15:49
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : run.py
# @Software : PyCharm

import pytest

pytest.main(["-s", "-v", "-m", "smoke", "--html=Outputs/report.html",
             "--reruns", "2", "--reruns-delay", "5"])  # 筛选
pytest.main()  # 无筛选