#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-27 21:21
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_08.py
# @Software : PyCharm

from selenium import webdriver
driver = webdriver.Chrome()
import time
# from selenium.webdriver.common.action_chains import ActionChains  #鼠标类
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait  #等待类
# from selenium.webdriver.support import expected_conditions as EC #条件
# from selenium.webdriver.common.keys import Keys
driver.get("https://tinypng.com/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="top"]/section/div[1]/section').click()
time.sleep(2)
import win32com.client
shell=win32com.client.Dispatch("WScript.shell")
shell.Sendkeys(r'D:\banner.png'+'\n')
