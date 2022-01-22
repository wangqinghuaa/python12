#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-03 22:55
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_01.py
# @Software : PyCharm

#相对路径  绝对路径
#E:\tmp\python11\python0103\class_01.py  #右键拷贝 copy path 绝对路径
#疑问：如果我们要打开一个文件 是需要绝对还是相对路径



#新建一个目录/新建一个文件夹 #在当前目录下新建一个Lina的文件夹
# os.mkdir("Lina")

#跨级新建目录  如果没有主目录会报错：系统找不到指定的路径 (跨级：保证前一个存在)
# #用/来代表路径的不同层级
# del "Lina/mor"#相对路径
# res=open("test.txt","w")
# res.write("12345678")
# path=os.getcwd()
# print(path)
#
# path_2=os.path.realpath(__file__)
# print("获取到当前路径是：{}".format(path_2))

# new_path_1=os.getcwd()+"\python1"
# print(new_path_1)
# os.mkdir(new_path_1)

#罗列出当前路径的所有文件和目录
# print(os.listdir(os.getcwd()))


# for path in os.listdir(os.getcwd()):
#     if os.path.isdir(path):
#         os.listdir(os.path.join(os.getcwd(),path))
#         print("{}还需要做进一步处理".format(path))
#     else:
#         print("这个是已经穷尽的路径",os.path.join(os.getcwd(),path))


# import os
# try:
#     os.rmdir("Lina")
# except Exception as e:
#     print("这类有可能报错了")
#     print("错误为：{0}".format(e))
#     file=open("error.txt","a+",encoding="utf-8")
#     file.write(e)
#     file.close()
#
# else:   #报错后不会被执行后面的代码
#     print("我就是这么厉害")



# for a in range(9):
#     for b in range(1,a+1):
#        print("{}*{}={}".format(b,a,a*b),end=" ")
#     print("")


# aa=[4,8,9,2,1,6,0]
# new_bb=[]
# for i in aa:
#     if i not in new_bb:
#         new_bb.append(i)
# print(new_bb)


# for a in range(len(aa)-1):     #打印有多少个下标元素：0，1，2，3，4
#     for b in range(len(aa)-1): #还是打印有多少个下表元素：其实就是简写：
#         if aa[b]>aa[b+1]:
#             aa[b],aa[b+1]=aa[b+1],aa[b]
# print(aa)
# a  0 1 2 3 4 0    4  8  9  2 1 6
# b  1 2 3 0 1 0    8  9  2  4 1 6


# 自动贩卖机：只接受1元，5元，10元的纸币或硬币，可以1块，5块，10块，最多不超过10元
#饮料只有橙汁、椰汁、矿泉水、早餐奶
#售价分别是：3.5，4，2，4.5
#写一个函数用来表示贩卖机的功能：
#用户投钱和选择饮料，并通过判断之后，给用户吐出来饮料和找零
# def aut_buy():
#     drinks={"1":3.5,"2":4,"3":2,"4":4.5}
#     #用户选择饮料
#     total=0 #总金额
#     while True:
#         choose=input("请选择你要购买的饮料：1 橙汁,2 椰汁, 3 矿泉水, 4 早餐奶，q 退出",)
#         if choose in drinks.keys():
#             total += drinks[choose]
#         elif choose=="q":
#                 print("退出选择饮料")
#                 break
#         else:
#             print("不存在该选项，请重新选择！")
#
#     #用户投币
#     toubi=0 #投币总金额
#     while True:
#         money = input("请投币：温馨提示-只接收1元，5元，10元的纸币或硬币，按q退出投币！")
#         if money=="1" or money=="5" or money=="10":
#             toubi += int(money)
#             if toubi>total:
#                 print("您刚刚购买了{0}元饮料，您已支付{1}元，找零{2}元".format(total,toubi, toubi-total))
#                 break
#             if toubi<total:
#                 print("您刚刚购买了{0}元饮料，您已支付{1}元，还需支付{2}元".format(total, toubi, total - toubi))
#             if toubi==total:
#                 print("您刚刚购买了{0}元饮料，您已支付{1}元，已支付完毕！".format(total, toubi,))
#                 break
#         elif money=="q":
#                 break
#         else:
#                 print("不存在该选项，请重新选择！")
#
#
# aut_buy()



def make_sandwich(*args):
    print("您的三明治包含了{}".format(args))

make_sandwich("生菜","培根","鸡蛋")