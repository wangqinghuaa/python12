#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-27 11:31
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : class_04.py
# @Software : PyCharm

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
import time
from selenium.webdriver.common.action_chains import ActionChains  #鼠标类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  #等待类
from selenium.webdriver.support import expected_conditions as EC #条件
from selenium.webdriver.common.keys import Keys



driver.get("https://www.baidu.com/")
driver.maximize_window()

element=driver.find_element_by_id("kw")
element.send_keys("selenium webdriver",Keys.ENTER)
element.send_keys(Keys.CONTROL,"c")
loc=(By.XPATH,'//*[@id="u1"]/span[@id="s-usersetting-top"]')
ele=driver.find_element(*loc)
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
ActionChains(driver).move_to_element(ele).perform()
#
# driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[2]').click()

