#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from time import ctime
import ntplib


def ntp_client(ntp_server):
    ntp = ntplib.NTPClient()
    try:
        response = ntp.request(ntp_server, version=3)
        print('同步时间：', ctime(response.tx_time))
    except:
        print(ntp_server, '无响应，请更换地址后再进行尝试！')


if __name__ == '__main__':
    ntp_client('ntp.aliyun.com')
