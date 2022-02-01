#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-18 21:39
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : send_email.py
# @Software : PyCharm



import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 邮件发送的用户名和密码  常识：第三方授权码
user="867075698@qq.com"
pwd="rxmkbpuewfodbfah"

now=time.strftime("%Y-%m-%d-%H:%M:%S") #获取时间戳


class SendEmail:
    def send_email(self, email_to, file_path):
        #email_to收件方
        #filepath你要发送邮件的地址
        #如名字所示Multipart就是分多个收件人,通过join将列表转换，以;为间隔的字符串
        msg = MIMEMultipart()
        msg["Subject"] = "二毛的测试报告 "+now
        msg["From"]=user
        msg["To"]=";".join(email_to)

        #这是文字部分
        part=MIMEText("这是自动化测试结果，请查收！")
        msg.attach(part)


        #加多个附件地址
        # path=["1","2","3","4"]
        # for item in path:
        #     part = MIMEApplication(open(item, "rb").read())
        #     part.add_header("Content-Disposition", "attachment", filename=file_path)
        #     msg.attach(part)

        #这是附件部分=针对一个附件处理
        part=MIMEApplication(open(file_path,"rb").read())
        part.add_header("Content-Disposition","attachment",filename=file_path)
        msg.attach(part)
        s=smtplib.SMTP_SSL("smtp.qq.com",timeout=30) #连接smtp邮件服务器，端口默认是25
        s.login(user,pwd)#登录服务器
        s.sendmail(user,email_to,msg.as_string())#发送邮件：发件方-收件方
        s.close()

if __name__ == '__main__':
    SendEmail().send_email(["451416191@qq.com","wqh18530929470@163.com"],r"E:\tmp\python11\python0109\test.report.html")





# import smtplib
# import base64
# import time
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# class Send_Email:
#
#     @staticmethod
#     def send_email(addressees): #可以传收件人
#
#         sender = '18530929470@163.com'  #邮箱用户名
#         mailserver = "smtp.163.com"  #邮箱服务器地址
#         password = 'UVHDSZLVUDNQZVCI'   #邮箱密码：需要使用授权码
#         now=time.strftime("%Y-%m-%d %H:%M:%S") #获取时间戳
#
#         #163和QQ邮箱收件人都可以，这样只能写一个收件人，发给163邮箱查看会好点-和HTML报告一样
#         receiver=";".join(addressees)
#
#
#         mail = MIMEMultipart()
#         file=r'E:\tmp\python11\python0109\test.report.html'
#         att = MIMEText(open(file, 'rb').read(),"base64", "utf-8")
#         att["Content-Type"] = 'application/octet-stream'
#
#         #这行是附件格式处理--针对QQ
#         new_file='=?utf-8?b?' + base64.b64encode(file.encode()).decode() + '?='
#         att["Content-Disposition"] = 'attachment; filename="%s"'%new_file
#         mail.attach(att)
#         mail.attach(MIMEText('这是一封带有附件的邮件,test.api测试报告'))# 邮件正文
#         mail['Subject'] = 'KPR自动申请测试报告 '+now  # 邮件主题
#
#
#         smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
#         # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
#         smtp.login(sender,password)  # 登录邮箱
#         smtp.sendmail(sender,addressee,mail.as_string())
#         smtp.quit()
#
# Send_Email.send_email(["wqh18530929470@163.com","867075698@qq.com"])





