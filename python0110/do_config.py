#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-10 21:37
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : do_config.py
# @Software : PyCharm


#配置文件
#properties config ini log4j 以这些结尾的都是配置文件
#configparser可以读取配置文件的信息
#有三个区域，section  option  value
import configparser

cf=configparser.ConfigParser()
cf.read("case.config",encoding="utf-8")
#读取数据方法1和2
res=cf.get("MODE","modes")
res_1=cf["MODE"]["mode"]
print(res_1)
#print(cf.sections()) #获取key
#print(cf.items("MODE")) #获取这个key所有的内容
#print(type(cf.get("MODE","mode")))#eval()转换我们原有的类型
