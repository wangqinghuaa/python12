#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-17 21:10
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : do_mysql.py
# @Software : PyCharm





import mysql.connector


db_config={'host': 'localhost',
    'user': 'root',
    'password': '13800wqh',
    'port': 3306,
    'database': 'plesson',
    'charset': 'utf8'}


#创建一个数据库连接
cnn=mysql.connector.connect(**db_config)

#游标
cursor=cnn.cursor()

#写sql语句
# select_sql='select * from students where name="李元芳"'
# select_sql='select max(score) from students'
select_sql='select max(score) from students where score like"9%"'

#执行
cursor.execute(select_sql)

#获取结果-打印
res=cursor.fetchone()#针对一行数据，元组
# res=cursor.fetchall()#针对一行数据，列表
print(res)
print(int(res[0])+1)  #拿到最大的加1

#关闭游标
cursor.close()
#关闭连接
cnn.close()


#特别提示：如果数据库拒绝访问：关闭一个数据库服务重新尝试就OK
