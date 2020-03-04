#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from scapy.all import *
import re
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错


def pcap_parser(filename, keyword):
    # 本代码主要任务: 搜索PCAP文件里边的所有数据包,找到匹配关键字的数据包
    pkts = rdpcap(filename)  # 使用scapy的rdpcap函数打开pcap文件
    return_pkts_list = []  # 返回匹配数据包的清单！
    for pkt in pkts.res:  # 遍历每一个数据包
        try:
            pkt_load = pkt.getlayer('Raw').fields['load'].decode().strip()  # 提取负载内容
            re_keyword = '.*' + keyword + '.*'
            # 如果负载内容匹配，并且源端口为23，把数据包添加到return_pkts_list
            if re.match(re_keyword, pkt_load) and pkt.getlayer('TCP').fields['sport'] == 23:
                return_pkts_list.append(pkt)
        except:
            pass
    return return_pkts_list  # 返回匹配数据包的清单！


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 搜索PCAP文件"login_invalid.pcap"中,出现invalid关键字的数据包
    pkts = pcap_parser("login_invalid.pcap", 'invalid')
    i = 1
    for pkt in pkts:
        print('==================第' + str(i) + "个包==================")
        pkt.show()
        i += 1
