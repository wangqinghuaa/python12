#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-22 10:53
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : tanboy.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup

url="https://www.youtube.com/c/tanboykun/videos"
myheader={"User-Agent":"Chrome/96.0.4664.45"}
result=requests.get(url,headers=myheader,)
html=result.text
print(html)
soup=BeautifulSoup(html,"lxml")#需要传递2个参数
r=soup.find_all("div",id="meta")
# print(r)
# book_list=soup.find_all("li",class_="yt-simple-endpoint")
# for book in book_list:
#     title=book.find("a",class_="fleft").text
#     author=book.find("p",class_="subject-abstract").text.strip()
#     price=book.find("span",class_="buy-info").find("a").text
#     print(title,author,price)
#     print("*"*10)