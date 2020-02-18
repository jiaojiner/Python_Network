#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
from Tools.GET_IFNAME import get_ifname


def get_ip_address(ifname):
    return ifaddresses(get_ifname(ifname))[AF_INET][0]['addr']


def get_ipv6_address(ifname):
    return ifaddresses(get_ifname(ifname))[AF_INET6][0]['addr']


if __name__ == "__main__":
    # print(get_ip_address('WLAN'))
    # print(get_ipv6_address('WLAN'))
    print(get_ip_address('ens33'))
    print(get_ipv6_address('ens33'))