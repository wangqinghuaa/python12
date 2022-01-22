#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-08 17:37
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_05.py
# @Software : PyCharm


import requests


url = "http://localhost:8066/api/mgr/loginReq"
data={"username":"auto","password":"sdfsdfsdf"}
res =requests.post(url,data)#消息实体，包含：响应头 响应码 响应正文 sessionid
# print("响应头：",res.headers)
# print("响应码：",res.status_code)
# print("相应正文：",res.text) #返回字符串
# print(res.json()) #返回字典  只有json的返回值才支持 html xml不能转换json格式
# print(res.cookies)
# print(res.cookies['sessionid'])  #获取cookie里面的sessionid





#添加课程
header ={"User-Agent": "Mozilla/5.0"} #定制请求头
payload ={'action':'add_course',
          'data':'''{"name":"初中数学",
          "desc":"初中数学课程",
          "display_idx":2}'''}
datas ="http://localhost:8066/api/mgr/sq_mgr/"
ress =requests.post(datas,payload,headers=header,cookies=res.cookies)
print(ress.json())
print("代理user-agent:",ress.request.headers)




