#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-05 22:20
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_02.py
# @Software : PyCharm




# class Teacher():
#
#     def __init__(self,name,age=18):
#         self.name=name
#         self.age=age
#         self.height=180 #写死，初始化函数没有返回值
#
#     #方法/函数
#     def function_test(self,*args):
#         print ("{0}会功能测试,今年{1}岁,还会{2}".format(self.name,self.age,*args))
#
#     def TeacHer(self,game):
#         self.function_test("健身,会前端")
#         return ("{0}会玩{1},今年{2}岁,身高{3}".format(self.name,game,self.age,self.height))
#
# res=Teacher("damao").TeacHer("王者荣耀")
# print(res)


# class Robot_One:
#     def __init__(self,year,name):
#         self.year=year
#         self.name=name
#     def walking_on_ground(self):
#             print(self.name+"只能在平地上行走,有障碍物就会摔倒")
#     def robot_info(self):
#             print("{}年生产的机器人{},是中国研发的".format(self.year,self.name))
#
# class Robot_Two:
#     def __init__(self,year,name):
#         self.year=year
#         self.name=name
#     def walking_on_ground(self): #重写
#             print(self.name+"可以在平地上平稳的行走")
#     def walking_avoid_block(self):#拓展
#             print(self.name+"可以避开障碍物")
#
# class Robot_Three(Robot_One,Robot_Two):#第三代机器人继承第一第二机器人
#         def jump(self):
#             print(self.name+"可以单膝跳跃")
#
# t3=Robot_Three("2020","小明")
# t3.robot_info()




#超继承
class MathMethod:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print (self.a+self.b)
    def sub(self):
        return self.a-self.b

class MathMethod_1(MathMethod):
    def divide(self):#扩展
        return self.a*self.b
    def add(self): #重写
        super(MathMethod_1,self).add()#超继承：从字类找到父类 找到父类方法 调用add方法 也要保留父类的方法
        print(self.a*self.b)

MathMethod_1(5,6).add()#有99行相同 1行不同




# class User():
# #     def __init__(self,first_name,last_name,age,height,weight):
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age
# #         self.height=height
# #         self.weight=weight#(体重)
# #     def describe_user(self):
# #         print(self.last_name+self.first_name+'的客户信息:身高:{},年龄:{}'.format(self.height,self.age))
# #     def greet_user(self,content):
# #             print(self.last_name+self.first_name+content)#方法1  如果在别的地方也会用到 就用第一种 
# # # #复习点1 类里面有初始化函数 创建实例的时候 有几个参数 就传几个 
# # # #复习点2.调用函数的时候 实例调用 
# # tf=User("小明","王",25,"170","85")
# # tf.describe_user()
# # tf.greet_user("您好啊 欢迎光临")


#2.定义一个学生类
#1>有下面的类属性：姓名 ，年龄 ，成绩(语文 数学 英语)
# [每课成绩的类型为整数]都放在初始化函数里面
#2>类方法：
#a>获取学生的姓名：get_name() 返回类型str
#b>获取学生的年龄：get_age()  返回类型：int
#c>返回3门科目中最高的分数 get_course() 返回类型：int
#d>写好类以后 定义2个同学测试下：zm=Student("xiaoli",20,[50,60,70])

# class Student():
# #     def __init__(self,name,age,grade):
# #         self.name=name
# #         self.age=age
# #         self.grade=grade
# #     def get_name(self):
# #             return(self.name)
# #     def get_age(self):
# #         return (self.age)
# #     def get_course(self):
# #         return (max(self.grade))
# # zm=Student("小明",20,[20,30,40])
# # print("获取学生的姓名是:"+zm.get_name())
# # print("获取学生的年龄是:"+str(zm.get_age()))
# # print("返回3门科目中最高的分数是:"+str(zm.get_course()))



#第三题：按照以下要求定义一个游乐园门票类 并创建实例调用函数
#  完成儿童和大人的总票价统计(人数不定 由你输入)# 平日票价100元
#  周末票价为平日票价的120%# 儿童半价

# class Ticket:
#     def __init__(self,price=100):
#         self.price = price
#     def cost_ticket(self):
#         try:
#             day = int(input("您需要购买那天的票? 1-5 分别代表周一到周五  6-7代表周末两天"))
#             man = input("请输入您要购买的大人门票")
#             child =input("请输入您要购买的小孩人数的门票")
#             if day in range(1,6):
#                 total = int(man)*self.price+int(child)*self.price*0.5
#             elif day in range(6,8):
#                 total=int(man)*self.price*1.2+int(child)*self.price*1.2*0.5
#             else:
#                  print("您输入的选项不对")
#             return total
#         except Exception as e:
#             print("您输入的内容为{},请输入正确的值".format(e))
#
# total = Ticket().cost_ticket()
# print("您需要付款{}元".format(total))



# 第四题  游戏大战#人和机器猜拳游戏 写成一个类 有如下几个函数
#函数1 选择角色 1.曹操  2.张飞  3刘备#函数2 角色猜拳 1 剪刀 2 石头 3 布 玩家输入一个1-3的数字
#函数3 电脑出拳 随机产生1个1-3的数字 提示电脑出拳结果
#  角色和机器出拳对战 对战结束后 最后出示本局的对战结果 赢 输 然后提示用户是否继续？ 按y继续 按n退出
#  最后结束的时候输出结果 角色赢几局  电脑赢几局 平局几次  游戏结束

# import random
# class game:
#     role_dict={1:"曹操",2:"张飞",3:"刘备"}
#     fist_dict={1:"剪刀",2:"石头",3:"布"}
#     def get_role_name(self): #获取角色
#         role_num =input('请输入您的角色1:"曹操",2:"张飞",3:"刘备"')
#         return self.role_dict[int(role_num)]
#     def get_role_fist(self): #角色出拳
#         fist_num=input('请出拳:1:"剪刀",2:"石头",3:"布"')
#         return int(fist_num)
#     def get_computer_fist(self): #电脑出拳
#         fist_num=random.randint(1,3)#从1-3随机选择
#         return fist_num
#     def play_games(self): #人机对战
#         role_win=0  #记录角色赢了
#         cp_win=0 #记录电脑赢了
#         draw=0 #记录平局
#         role_name=self.get_role_name() #获取角色名
#         print("{}请出拳".format(role_name))
#         while True:
#             role_fist=self.get_role_fist() #角色出拳
#             computer_fist=self.get_computer_fist() #机器人出拳
#             print(role_name+"出拳为{0},电脑出拳为{1}".format(self.fist_dict[role_fist],self.fist_dict[computer_fist]))
#             if role_fist-computer_fist==1 or role_fist-computer_fist==-2:
#                 role_win+=1 #角色赢
#                 print("角色赢了")
#             elif role_fist-computer_fist==-1 or role_fist-computer_fist==2:
#                 cp_win+= 1  # 电脑赢
#                 print("电脑赢了")
#             elif role_fist-computer_fist==0:
#                 draw+=1 #平局
#                 print("平局")
#                 choose = input("您是否要继续？按y继续，按n退出")
#                 if choose=="n":
#                     break
#         print("角色赢了{}局,电脑赢了{}局,平局{}".format(role_win,cp_win,draw))
# if __name__=="__main__":
#         game().play_games()