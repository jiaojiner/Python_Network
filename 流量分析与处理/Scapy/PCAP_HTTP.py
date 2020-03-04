#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from scapy.all import *
import re
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 清除报错


def findpcapuri(pcap_filename, host_regex):
    # 本代码主要任务: 搜索PCAP文件里边的所有数据包,找到HTTP Host字段匹配正则表达式host_regex的HTTP请求数据包
    # 并收集这个HTTP请求的Host, URI , User_Agent字段
    pkts_file = rdpcap(pcap_filename)  # 使用scapy的rdpcap函数打开pcap文件
    pkt_list = pkts_file.res  # 提取每一个包到清单pkt_list
    result_list = []
    for packet in pkt_list:  # 分析每一个数据包
        try:
            if packet.getlayer(TCP).fields['dport'] == 80:  # 分析TCP目的端口为80的数据包
                http_request = packet.getlayer(Raw).fields['load'].split()
                # packet.show()
                Host_location = http_request.index(b'Host:') + 1  # 找到出现b'Host:'的下面一个位置
                Host = http_request[Host_location]  # 提取HTTP的host
                Host_ACSII = Host.decode()  # 解码为普通字符串
                if re.search(host_regex, Host_ACSII):  # 搜索匹配正则表达式的host
                    # print(re.search(host_regex, Host_ACSII))
                    URI_location = http_request.index(b'GET') + 1
                    User_Agent_location = http_request.index(b'User-Agent:') + 1
                    URI = http_request[URI_location]  # 找到URI
                    User_Agent = http_request[User_Agent_location]  # 找到User Agent
                    result_list.append((Host, URI, User_Agent))  # 添加Host,URI和User_Agent到列表

        except:
            pass
    return result_list


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    result = findpcapuri("dos.pcap", 'sina\.com\.cn')

    # 对找到数据包进行展示,打印Host, URI , User_Agent
    # for http_info in result:
    #     print('====================================================================')
    #     print(b'Host: ' + http_info[0])
    #     print(b'URI: ' + http_info[1])
    #     print(b'User_Agent: ' + http_info[2])

    # 展示所有host, 使用集合技术, 去除重复部分
    host_list = []
    for http_info in result:
        host_list.append(http_info[0])
    # print(host_list)
    print([i.decode() for i in list(set(host_list))])  # 使用集合技术,找到不重复的Host
