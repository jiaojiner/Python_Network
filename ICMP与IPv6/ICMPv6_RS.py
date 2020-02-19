#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

# IPv6参考文档
# https://www.idsv6.de/Downloads/IPv6PacketCreationWithScapy.pdf
# https://www.ernw.de/download/Advanced%20Attack%20Techniques%20against%20IPv6%20Networks-final.pdf

# 微软默认并不使用EUI64地址,而是随机产生
# https://www.dan.me.uk/blog/2011/02/10/windows-7-ipv6-auto-assignment-fix/
# netsh interface ipv6 set privacy state=disabled store=active
# netsh interface ipv6 set privacy state=disabled store=persistent
# netsh interface ipv6 set global randomizeidentifiers=disabled store=active
# netsh interface ipv6 set global randomizeidentifiers=disabled store=persistent

from scapy.layers.inet6 import IPv6, ICMPv6ND_RS, ICMPv6NDOptSrcLLAddr
from scapy.sendrecv import sr1
from Tools.GET_MAC_netifaces import get_mac_address
from Tools.IPv6_Tools import mac_to_ipv6_linklocal
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错


def icmpv6_rs(ifname):
    ll_mac = get_mac_address(ifname)  # 获取本机接口MAC地址
    # -----------IPv6头部------------
    # Next Header: 0x3A (ICMPv6)
    # 原地址: Link Local address
    # 目的地址: FF02::2(所有路由器)
    base = IPv6(src=mac_to_ipv6_linklocal(ll_mac), dst='ff02::2')
    # ----------ICMPv6头部----------
    # ICMPv6 Type: 133
    # ICMPv6 Code: 0 (RS)
    router_solicitation = ICMPv6ND_RS()
    # ----Source Link-Layer Address----
    # 源地址: 本地MAC地址
    src_ll_addr = ICMPv6NDOptSrcLLAddr(lladdr=ll_mac)
    # 构建数据包
    packet = base / router_solicitation / src_ll_addr
    # packet.show()
    # 发送数据包,接受返回数据包
    result = sr1(packet, timeout=2, verbose=False)
    # result.show()
    # 提取返回数据包中的网关MAC
    print("gwmac: ", result.getlayer("ICMPv6 Neighbor Discovery Option - Source Link-Layer Address").fields['lladdr'])
    # 提取返回数据包中的MTU
    print("mtu: ", result.getlayer("ICMPv6 Neighbor Discovery Option - MTU").fields['mtu'])
    # 提取返回数据包中的Prefix信息
    print("prefix: ", result.getlayer("ICMPv6 Neighbor Discovery Option - Prefix Information").fields['prefix'])


if __name__ == '__main__':
    # Windows Linux均可使用
    icmpv6_rs("ens33")
