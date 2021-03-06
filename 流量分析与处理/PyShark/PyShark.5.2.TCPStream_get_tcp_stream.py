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


def get_tcp_stream(pcapfile, id):
    # 提取PCAP文件中,特定tcp流ID的数据包
    tcp_stream_pkt_list = []  # 最终返回的特定流ID的数据包清单

    cap = pyshark.FileCapture(pcapfile, keep_packets=False)  # 打开PCAP文件

    for pkt in cap:  # 遍历包
        try:
            if str(pkt.tcp.stream) == str(id):  # 把特定流ID的数据包放入清单
                tcp_stream_pkt_list.append(pkt)
        except:
            pass
    return tcp_stream_pkt_list  # 返回清单


if __name__ == '__main__':
    i = 1
    for pkt in get_tcp_stream('dos.pcap', 10):
        print('='*30, i, '='*30)
        pkt.pretty_print()
        i += 1
