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


def get_max_id(pcapfile):
    # 本代码的主要任务: 找到最大的TCP Stream ID! 这个ID是连续的!
    cap = pyshark.FileCapture(pcapfile, keep_packets=False)

    sess_index = []  # 所有的tcp流索引ID清单

    for pkt in cap:
        try:
            sess_index.append(pkt.tcp.stream)  # 把所有的tcp流索引ID放入清单
        except:
            pass

    if len(sess_index) == 0:  # 如果没有任何索引ID就打印错误
        print('No TCP Found')
    else:
        sess_index_int = [int(sid) for sid in sess_index]  # 把索引ID字符串转换为整数,便于排序

    return sess_index, max(sess_index_int)  # 返回最大的索引ID


if __name__ == '__main__':
    print(get_max_id('dos.pcap'))
