#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-15 9:02
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : get_cookie.py
# @Software : PyCharm

class GetCookie:
    Cookie=None

setattr(GetCookie,"Cookie","123456")  #setattr 设置属性值
print(hasattr(GetCookie,"Cookie"))    #hasattr 判断是否有这个属性值
# delattr(GetCookie,"Cookie")  #del删除这个属性值
print(hasattr(GetCookie,"Cookie"))    #hasattr 判断是否有这个属性值
print(getattr(GetCookie,"Cookie"))    #get 获取属性值