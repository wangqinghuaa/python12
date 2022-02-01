#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-27 19:28
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_07.py
# @Software : PyCharm


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  #等待类
from selenium.webdriver.support import expected_conditions as EC #条件
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://www.12306.cn/index/")

time.sleep(5)
#出发地
js_1='var a=document.getElementById("fromStationText");a.readOnly=false;a.value="郑州";'
driver.execute_script(js_1)

time.sleep(5)
#到达地
js_2='var a=document.getElementById("toStationText");a.readOnly=false;a.value="北京";'
driver.execute_script(js_2)

time.sleep(3)

#出发日期
js_3='var a=document.getElementById("train_date");a.readOnly=false;a.value="2022-02-02";'
driver.execute_script(js_3) #arguments接收外部参数，列表[]
time.sleep(0.5)
#点击查询
driver.find_element_by_xpath('//*[@id="search_one"]').click()

#通过手动输入把12306不能手动改的日期给改了




