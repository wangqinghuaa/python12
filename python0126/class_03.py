#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-27 10:13
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_03.py
# @Software : PyCharm


from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://music.163.com/#/discover/toplist?id=3779629')
# 切换到ifram里面
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="contentFrame"]'))


res=driver.find_element_by_xpath('//*[@class="m-table m-table-rank"]//*[@class="ttc"]//span//*[@title="留香"]')
print(res.text)

