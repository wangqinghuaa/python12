#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-21 22:44
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : douban.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup

url="https://book.douban.com/chart?subcat=F&icn=index-topchart-fiction"
myheader={"User-Agent":"Chrome/96.0.4664.45"}
result=requests.get(url,headers=myheader)
html=result.text

soup=BeautifulSoup(html,"lxml")#需要传递2个参数
r=soup.find_all("a",class_="fleft")
book_list=soup.find_all("li",class_="media")
print(book_list)
for book in book_list:
    title=book.find("a",class_="fleft").text
    author=book.find("p",class_="subject-abstract").text.strip()
    price=book.find("span",class_="buy-info").find("a").text
    print(title,author,price)
    print("*"*10)



