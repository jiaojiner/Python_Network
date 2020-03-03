#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sendp, srp
from Tools.GET_MAC_netifaces import get_mac_address
from Tools.Change_MAC_To_Bytes import Change_MAC_To_Bytes
from Tools.Scapy_IFACE import scapy_iface  # 获取scapy iface的名字
import time
import struct
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错

# Dynamic Host Configuration Protocol (DHCP) and Bootstrap Protocol (BOOTP) Parameters
# https://www.iana.org/assignments/bootp-dhcp-parameters/bootp-dhcp-parameters.xhtml
requested_option_1 = 1   # Subnet Mask
requested_option_2 = 6   # Domain Name Servers
requested_option_3 = 15  # Domain Name
requested_option_4 = 44  # NetBIOS (TCP/IP) Name Servers
requested_option_5 = 3   # Routers
requested_option_6 = 33  # Static Routes
requested_option_7 = 150  # TFTP Server address
requested_option_8 = 43  # Vendor Specific Information

bytes_requested_options = struct.pack("8B", requested_option_1,
                                            requested_option_2,
                                            requested_option_3,
                                            requested_option_4,
                                            requested_option_5,
                                            requested_option_6,
                                            requested_option_8,
                                            requested_option_7)
# print(bytes_requested_options)


def chaddr(info):
    # chaddr一共16个字节，正常的chaddr信息里边只有MAC地址,思科比较特殊
    # MAC地址只有6个字节，所以需要把剩余部分填充b'\x00'
    return info + b'\x00' * (16 - len(info))


def DHCP_Discover_Sendonly(ifname, MAC, wait_time=2):
    Bytes_MAC = Change_MAC_To_Bytes(MAC)  # 把MAC地址转换为二进制格式
    # param_req_list为请求的参数，没有这个部分服务器只会回送IP地址，什么参数都不给
    discover = Ether(dst='ff:ff:ff:ff:ff:ff',
                     src=MAC,
                     type=0x0800) / IP(src='0.0.0.0',
                                       dst='255.255.255.255') / UDP(dport=67,
                                                                    sport=68) / BOOTP(op=1,
                                                                                      chaddr=chaddr(Bytes_MAC)) / DHCP(
                                                                                                                        options=[('message-type', 'discover'),
                                                                                                                                 ('param_req_list',
                                                                                                                                  bytes_requested_options),
                                                                                                                                 ('end')])
    # # discover.show()
    # discover_result = srp1(discover)
    # discover_result.show()
    # result = scapy_iface(ifname)
    # print(result)
    if wait_time != 0:
        time.sleep(wait_time)
        sendp(discover,
              iface=scapy_iface(ifname),
              verbose=False)
    else:
        sendp(discover,
              iface=scapy_iface(ifname),
              verbose=False)


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    Local_MAC = get_mac_address('WLAN')
    # print(Local_MAC)
    DHCP_Discover_Sendonly('WALN', Local_MAC)
