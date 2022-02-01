#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-27 17:46
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_06.py
# @Software : PyCharm

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  #等待类
from selenium.webdriver.support import expected_conditions as EC #条件
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)


#js 将元素拖动到可视区域；
# loc=(By.XPATH,'//*[@id="page"]/div/a[1]/span') #需要指定元素，滚动到最底部
loc=(By.XPATH,'//*[@id="8"]/div/div/article/section/a/h3/span')  #滚动到指定元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
a=driver.find_element(*loc)

#js函数-元素对象 scrollintoview();

driver.execute_script('arguments[0].scrollIntoView(false);',a)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') #不用指定元素
# time.sleep(1)
# driver.execute_script('window.scrollTo(document.body.scrollHeight,0)') #不用指定元素

#通过手动输入把12306不能手动改的日期给改了
# js="var a=document.getElementById(\"train_date\");a.readOnly=false;a.value=\"2022-02-02\";"
js="var a=arguments[0];a.readOnly=false;a.value=\"2022-02-02\";"
loc=("xpath","//*[@#='train_date']")

