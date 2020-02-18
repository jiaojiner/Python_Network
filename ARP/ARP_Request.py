#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


from scapy.layers.l2 import ARP
from scapy.sendrecv import sr1
from Tools import GET_MAC_netifaces, GET_IP_netifaces


def arp_request(dst, ifname):
    hwsrc = GET_MAC_netifaces.get_mac_address(ifname)
    psrc = GET_IP_netifaces.get_ip_address(ifname)
    try:
        arp_pkt = sr1(ARP(op=1, hwsrc=hwsrc, psrc=psrc, pdst=dst), timeout=5, verbose=False)
        return dst, arp_pkt.getlayer(ARP).fields['hwsrc']
    except AttributeError:
        return dst, None


if __name__ == '__main__':
    arp_result = arp_request('192.168.98.128', 'ens33')
    print('主机：', arp_result[0], 'MAC地址为：', arp_result[1])
