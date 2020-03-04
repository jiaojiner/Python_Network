#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

# pyshark 特点分析
# 1.解码能力强,提供丰富的字段,远远强于Scapy
# 2.能够直接使用wireshark强大的display_filter
# 3.能够找到现象级数据包,例如重传 display_filter='tcp.analysis.retransmission'
# 3.能够使用wireshark的follow tcp stream的技术,找到特定tcp stream的数据包

# pyshark 问题
# 抓包在3.6以上环境出现问题
# 不能保存分析后的数据包到PCAP

import pyshark


pkt_list = []

# 分析现象级数据包,"tcp重传的数据包"
cap = pyshark.FileCapture('dos.pcap', keep_packets=False, display_filter='tcp.analysis.retransmission')


def print_highest_layer(pkt):
    # 通过过滤得到数据包清单
    pkt_list.append(pkt)


cap.apply_on_packets(print_highest_layer)

# pretty_print TCP重传的数据包
for x in pkt_list:
    print('='*80)
    # pretty_print() 和wireshark GUI类似的解码效果
    x.pretty_print()
