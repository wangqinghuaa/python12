#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-25 17:36
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_01.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  #等待类
from selenium.webdriver.support import expected_conditions as EC #条件
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(10)
driver.find_element(By.ID,"kw").send_keys("selenium")
driver.find_element(By.ID,"su").click()

loc=(By.XPATH,'//*[@id="1"]/div/div/h3/a')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))  #指定元素可见(用的最多)
# WebDriverWait(driver,10).until(EC.presence_of_element_located)  #指定元素存在
driver.find_element_by_xpath('//*[@id="1"]/div/div/h3/a').click()

handle = driver.current_window_handle

#切换窗口-会产生一个新的句柄-最先打开的是第一个

wins=driver.window_handles #获取所有句柄-窗口
print(wins)
driver.switch_to.window(wins[-1]) #切换到最后一个窗口
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchLemma"]').click()#触发新的窗口






time.sleep(50)
driver.quit()