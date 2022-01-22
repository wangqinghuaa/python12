#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-03 20:32
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : do_file.py
# @Software : PyCharm

#处理文件：读取存文件,默认是r
#file  xml  html  txt

#read  write  append(读写追加)
# r   w   a   r+：可读可写    w+   a+
# rb  rb+  wb  wb+ ab  ab+
#1. file文件open之后默认是r 只读模式，如果要写会报错
# file=open("python11.txt",mode="a",encoding="utf-8")
# res=file.writelines("\n777889")
# print(res)

# for i in range(6):
#     print("*"*i)

#输入一个由*组成的直角和等腰三角形
# for i in range(6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("")
#
# for i in range(1,6):#控制行数
# #     #一个for循环控制#符合输出
# #     #一个for循环控制*的输出
# #     for j in range(1,6-i):#控制@符号 4 3 2 1 0
# #         print(" ", end='')
# #     for k in range(1,i+1):
# #         print("*  ",end='')
# #     print("")


import random
# aa=[2,4,7,9,6,1,0]
# random.shuffle(aa)
# print(aa)
# aa.sort()
# aa.sort(reverse=False)
# print(aa)

# for a in range(0,len(aa)):
#     for b in range(0,len(aa)-1):
#         if aa[b] > aa[a]:
#              aa[b], aa[a] = aa[a], aa[b]
# print(aa)

#去重并且从小到大排列
a=[4,5,6,7,5,4,3]
# new=list(set(a))
# print(new)


new_list=[]
for i in a:
    if i not in new_list:
        new_list.append(i)
print(new_list)