#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import netifaces
from Tools.GET_IFNAME import get_ifname


def get_mac_address(ifname):
    # print(netifaces.ifaddresses(get_ifname(ifname))[netifaces.AF_LINK])
    return netifaces.ifaddresses(get_ifname(ifname))[netifaces.AF_LINK][0]['addr']


if __name__ == '__main__':
    # print(get_mac_address("ens33"))
    print(get_mac_address("WLAN"))
