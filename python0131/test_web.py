#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-31 23:22
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_web.py
# @Software : PyCharm


import time
import pytest
from selenium import webdriver

# 定义一个fixture
# @pytest.fixture
# def init():
#     #前置
#     print("***我是函数级别的前置***")
#     driver = webdriver.Chrome()
#     driver.get("http://www.baidu.com")
#     yield driver, True #分割线
#     #后置
#     print("***我是函数级别的后置***")
#     driver.quit()

# 定义类级别
@pytest.fixture(scope="class")
def mycc():
    print("我是类级别的前置")
    yield
    print("我是类级别的后置")


# 测试用例
def test_baidu():
    print("1111111111")


@pytest.mark.usefixtures("mycc")
def test_taobao():
    print("****taobao****")


# @pytest.mark.usefixtures("init") # 夹的是测试类/方法
@pytest.mark.usefixtures("mycc")
class TestApi:

    def test_aa(self):
        print("***test_aa***")

    # @pytest.mark.smoke
    def test_bb(self):
        print("***test_bb***")

    def test_baidu(self,init):  #有参数，是数据驱动还是fixture/会自动去找，
        print("***test_baidu***")
        time.sleep(1)
        init[0].find_element_by_id("kw").send_keys("selenium")
        time.sleep(1)
        # init[1].find_element_by_id("kw").send_key("selenium") #多个返回值通过下标取值


