#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-26 20:31
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : study_mock.py
# @Software : PyCharm

#代替第三方支付接口：包含url,data,method,返回参数

from unittest import mock
import requests

def request_baidu():
    return requests.get("https://www.baidu.com/").text.encode('utf-8')

def print_baidu():
    print(request_baidu())

request_baidu=mock.Mock(return_value="this is baidu")#代替request_baidu方法的返回值
print_baidu()

