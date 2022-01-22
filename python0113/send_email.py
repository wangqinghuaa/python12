#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-18 21:39
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : send_email.py
# @Software : PyCharm

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-18 22:04
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : send_email.py
# @Software : PyCharm



# import smtplib
# # import time
# # from email.mime.multipart import MIMEMultipart
# # from email.mime.text import MIMEText
# # from email.mime.application import MIMEApplication
# #
# # #邮件发送的用户名和密码  常识：第三方授权码
# #
# # _user="867075698@qq.com"
# # _pwd="fc306a36d4004edeac6baa9e160b4f1a"
# #
# # now=time.strftime("%Y-%m-%d-%H_%M_%S") #获取时间戳
# #
# #
# # class sendEmail:
# #     def send_email(self,email_to,filepath):
# #         #email_to收件方
# #         #filepath你要发送邮件的地址
# #         #如名字所示Multipart就是分多个部分
# #         msg=MIMEMultipart()
# #         msg["Subject"]=now+"huazai的测试报告"
# #         msg["From"]=_user
# #         msg["To"]=email_to
# #
# #         #这是文字部分
# #         part=MIMEText("这次是自动化测试结果，请查收！ ")
# #         msg.attach(part)
# #
# #         #这是附件部分
# #         part=MIMEApplication(open(filepath,"rb").read())
# #         part.add_header("Content-Disposition","attachment",filename=filepath)
# #         msg.attach(part)
# #         s=smtplib.SMTP_SSL("smtp.qq.com",timeout=30) #连接smtp邮件服务器，端口默认是25
# #         s.login(_user,_pwd)#登录服务器
# #         s.sendmail("867075698@qq.com","451416191@qq.com",msg.as_string())#发送邮件
# #         s.close()
# #
# # if __name__ == '__main__':
# #     sendEmail().send_email("867075698@qq.com",r"E:\tmp\python_12\API_AUTO\test_result\http_report\test_api.html")



# import smtplib
# from email.mime.text import MIMEText
#
# mailserver = "smtp.163.com"  #邮箱服务器地址
# username_send = '18530929470@163.com'  #邮箱用户名
# password = 'UVHDSZLVUDNQZVCI'   #邮箱密码：需要使用授权码
# username_recv = '867075698@qq.com'  #收件人，多个收件人用逗号隔开
# mail = MIMEText(r'E:\tmp\python_12\API_AUTO\test_result\http_report\test_api.html')
# mail['Subject'] = '这是邮件主题'
# mail['From'] = username_send  #发件人
# mail['To'] = username_recv  #收件人；[]里的三个是固定写法，别问为什么，我只是代码的搬运工
# smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
# # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
# smtp.login(username_send,password)  #登录邮箱
# smtp.sendmail(username_send,username_recv,mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
# smtp.quit() # 发送完毕后退出smtp
# print ('success')



import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailserver = "smtp.163.com"  #邮箱服务器地址
username_send = '18530929470@163.com'  #邮箱用户名
password = 'UVHDSZLVUDNQZVCI'   #邮箱密码：需要使用授权码
username_recv = '867075698@qq.com'  #收件人，多个收件人用逗号隔开
mail = MIMEMultipart()
# file = r'E:\\testpy\\python-mpp\\day8\\练习\\sendmail.py'
# att = MIMEText(open(file,encoding='utf-8').read())  #这个只可以发送py或者txt附件，复杂一点的就会报错
file=r'E:\tmp\python_12\API_AUTO\test_result\http_report\test_api.html'
att = MIMEText(open(file, 'rb').read(),"base64", "utf-8")  #这个可以发送复杂的附件，比如附件为表格
att["Content-Type"] = 'application/octet-stream'

#这行是把附件的格式进行一些处理，不知道为啥要这么写，但是如果不写接收到的附件已经不是表格样式了
new_file='=?utf-8?b?' + base64.b64encode(file.encode()).decode() + '?='

att["Content-Disposition"] = 'attachment; filename="%s"'%new_file
mail.attach(att)
mail.attach(MIMEText('这是一封带有附件的邮件正文内容，假装很长'))#邮件正文的内容
mail['Subject'] = '这是邮件主题'
mail['From'] = username_send  #发件人
mail['To'] = username_recv  #收件人；[]里的三个是固定写法，
smtp = smtplib.SMTP(mailserver,port=25) # 连接邮箱服务器，smtp的端口号是25
# smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
smtp.login(username_send,password)  #登录邮箱
smtp.sendmail(username_send,username_recv,mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('success')





