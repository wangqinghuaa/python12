#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-02-01 13:13
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : conftest.py
# @Software : PyCharm


import pytest
from selenium import webdriver

# 定义一个fixture
@pytest.fixture
def init():
    #前置
    print("***我是函数级别的前置***")
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    yield driver, True #分割线
    #后置
    print("***我是函数级别的后置***")
    driver.quit()