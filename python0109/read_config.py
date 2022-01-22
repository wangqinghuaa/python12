#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-10 22:22
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : read_config.py
# @Software : PyCharm

import configparser
class Read_Config:
    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf.get(section,option)

if __name__ == '__main__':

    res=Read_Config().read_config("case.config","MODE","mode")
    print(res)