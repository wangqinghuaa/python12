#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     :2022-01-23 22:04
# @Author   :wangqinghua
# @Email    : 867075698@qq.com
# @File     : handle.py
# @Software : PyCharm

import requests
import time

HOST="http://127.0.0.1:9999"

#测试尽早介入：左移
# def test():
#     data={"key1":"value1","key2":"value2"}
    # res=requests.get("{0}/xt".format(HOST),json=data)

    # json={"user_id": "sq001","goods_id": "1234",
    #         "num": 1,"amount": 100.8}
    # res=requests.get("{0}/api/order/create/".format(HOST),json=json)

    # queries={"order_id": "6666"}
    # res=requests.get("{0}/api/order/get_result/".format(HOST),params=queries)
    # print("请求的内容是:{}".format(res.text))

# def order_api():#申请订单接口
#         headers={"Content-Type": "application/json"}
#         data={"user_id": "sq123456",
# 			"goods_id": "20200815",
# 			"num":1,
# 			"amount":200.6}
#         res=requests.post("{0}/api/order/create/".format(HOST),json=data,headers=headers)
#         print(res.text)

def list_add(interval=5,timeout=30):  #查询订单接口
    # orderid:申请id
    # interval:频率
    # timeout :超时时间
    startTime=time.time() #开始时间
    endTime=startTime+timeout #查询结束时间
    count=1 #查询次数
    while time.time()<endTime:
        data = {"order_id": "6666"}
        res = requests.get("{0}/api/order/get_result/".format(HOST), params=data)

        if res.text: #如果查询到结果就退出
            print("第{}次查询的结果是:{}".format(count,res.text))
            break
        else:
            print("第{}次查询结果，请等待".format(count))
        time.sleep(interval)
        count+=1
    print("---查询操作结束---")

#查询接口注意事项
#使用什么查询 id
#频率 interval
#查多久认为超时 timeout
if __name__ == '__main__':
    list_add()