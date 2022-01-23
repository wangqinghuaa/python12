#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-23 21:06
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : fakers.py
# @Software : PyCharm

from faker import Faker
from faker import Factory
fake = Faker(locale="en_US")
# print(fake.name())


# print(fake.address())
# print(fake.phone_number())
# print(dir(fake))

# for _ in range(1):
for _ in range(10):
    r=('姓名：', fake.name(), ' 手机号：', fake.phone_number())
    print(r)
