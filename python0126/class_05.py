#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-27 16:51
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_05.py
# @Software : PyCharm

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://management-system.pikachu.develop/#/")

driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/form/div[2]/div/div[1]/input').send_keys("kpr01")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/form/div[3]/div/div[1]/input').send_keys("aaa123")
time.sleep(1)
driver.find_element_by_tag_name("button").click()

#查找订单
time.sleep(5)
res=driver.find_element_by_xpath('//*[@id="page_main"]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody')

#点击查看详情  #   //*[contains(text(),"KPR-23022181629965128920")]
time.sleep(5)
if "KPRTR851310" in res.text:
    res=driver.find_element_by_xpath('//*[contains(text(),"KPRTR851310")]/../../../td[8]//*[@class="ivu-table-cell-slot"]//a[2]')
    res.click()

#切换句柄
all_header = driver.window_handles
driver.switch_to.window (all_header[1])

time.sleep(5)