#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from scapy.all import *
import hexdump
from Tools.Scapy_IFACE import scapy_iface
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错


def hexdump(src, length=16):  # 每16个字节被提取出来，进行16进制的decode
    for i in range(0, len(src), length):
        s = src[i:i + length]
        hexdump.hexdump(s)


string = b''


def telnet_monitor_callback(pkt):
    global string
    try:
        string = string + pkt.getlayer(Raw).fields['load']  # 提取Telnet中的数据，并且把他们拼在一起
    except Exception as e:
        pass


def telnet_monitor(user_filter, ifname):
    # 捕获过滤器匹配的流量, 对流量进行解码
    PTKS = sniff(prn=telnet_monitor_callback,
                 filter=user_filter,
                 store=1,
                 iface=scapy_iface(ifname),
                 timeout=60)

    wrpcap("telnet.cap", PTKS)  # 保持捕获的数据包到文件
    hexdump(string)  # 解码展示


if __name__ == "__main__":
    telnet_monitor('tcp port 23 and ip host 192.168.98.129', 'ens33')
