#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


from scapy.all import *
from Tools.GET_IFNAME import get_ifname
import platform
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错


def scapy_iface(os_name):
    if platform.system() == "Linux":
        return os_name
    elif platform.system() == "Windows":
        for x, y in ifaces.items():
            if y.pcap_name is not None:
                if get_ifname(os_name) == ('{' + y.pcap_name.split('{')[1]):
                    return x
                else:
                    pass


if __name__ == '__main__':
    # print(ifaces)
    print(scapy_iface('ens33'))
