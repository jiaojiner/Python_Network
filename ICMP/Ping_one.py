#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from scapy.layers.inet import IP, ICMP
from scapy.packet import Raw
from scapy.sendrecv import sr1
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错信息


def ping_one(dst):  # 构建函数
    ping_pkt = IP(dst=dst)/ICMP() / b'welcome!'  # 构建数据包，目的地址为dst，数据部分为字节字符串welcome！
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)  # 发送数据包并将返回结构赋值到ping_result中
    # print(ping_result.getlayer(Raw).fields['load'])
    try:
        if ping_result.getlayer(IP).fields['src'] == dst and ping_result.getlayer(ICMP).fields['type'] == 0 \
                and ping_result.getlayer(Raw).fields['load'] == b'welcome!':
            # 判断返回数据包是否为reply，通过源地址，返回数据与返回类型进行判断
            return dst, 1  # 如果为返回数据包，函数返回输入的目的地址与1
        else:
            return dst, 2  # 如果不是返回数据包，则函数2
    except Exception:  # 如果无法ping通，则不会有返回结果，会出现报错，如果产生报错，直接返回dst与2
        return dst, 2


if __name__ == '__main__':
    try:
        while True:
            dst = input('请输入目的IP地址:')
            if dst == '':
                print('目的地址为空，请重新输入！')
            else:
                break
        result = ping_one(dst)
        if result[-1] == 1:
            print('目的', result[0], '可达！')
        else:
            print('目的', result[0], '不可达！')
    except KeyboardInterrupt:
        print('成功接收信号，退户程序！')

