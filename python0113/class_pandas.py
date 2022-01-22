#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-15 9:15
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_pandas.py
# @Software : PyCharm


import pandas as pd
df=pd.read_excel("tests.xlsx",sheet_name="test")  #默认读取第一张表单,添加sheet_name指定表单
# print(df.values)  #获取全部，从索引0开始读取
# print(df.head())  #默认读取前5行
# print(df.values[0]) #获取某一行
# print(df.loc[2].values)#获取某一行
# print(df.values[1,2]) #获取第一行的第二个数据,获取指定行指定列
# print(df.values[[0,1,2]]) #获取多行
# print(df.cummax) #获取最大行列
# print(df.values[:2])#获取某一列
# print(df.values[:,3])#获取第三列的所有数据
# print(df.loc[1,["case_id","module","title","url","data","expected","method"]].to_dict())  #获取第一行转化成字典
# print(df.loc[1].to_dict())

#循环获取所有数据
test_data=[]
for i in df.index.values:
    row_data=df.loc[i].to_dict()
    test_data.append(row_data)

print(test_data)

