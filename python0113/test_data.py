#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-13 22:07
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : test_data.py
# @Software : PyCharm


import requests

#登录
loging_url="http://localhost:8066/api/mgr/loginReq"
login_data={"username": "auto", "password": "sdfsdfsdf"}

#列出课程
lists_url="http://localhost:8066/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20"

list_url="http://localhost:8066/api/mgr/sq_mgr/"
params={'action':'list_course','pagenum':1,'pagesize':20}
#第一种
s=requests.session() #创建了一个会话
#登录
res=s.post(loging_url,login_data)
print(res.json())
# 列出课程
lis=s.get(lists_url,params={})  #params={}可省略
print(lis.json())


#第二种
#登录
# res=requests.post(loging_url,login_data)
# cookies=res.cookies
# print(res.json())

#列出课程
# res_list=requests.get(list_url,params=params,cookies=cookies)
# print(res_list.json())