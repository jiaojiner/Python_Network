#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from Tools import GET_IP_netifaces
from Tools import GET_IP_IFCONFIG
from ARP import ARP_Request


def arp_free(ifname='ens33'):
    # localip = (GET_IP_IFCONFIG.get_ip(ifname))[-1]
    # print(localip)
    localip = GET_IP_netifaces.get_ip_address(ifname)
    print(localip)
    pkt = ARP_Request.arp_request(localip, ifname)
    if pkt[-1]:
        return pkt[0], pkt[-1]
    else:
        return pkt[0], None


if __name__ == '__main__':
    result = arp_free()
    if result[-1]:
        print('接口地址：', result[0], '与该设备', result[-1], '地址冲突！')
    else:
        print('接口地址不冲突，请放心使用！')
