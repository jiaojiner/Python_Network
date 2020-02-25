#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！
import random
import re
import struct
import time
from scapy.layers.inet import IP, ICMP
from scapy.packet import Raw, Padding
from scapy.sendrecv import sr1


def ping_one(dst, id_ping, seq_ping, ttl_ping):
    send_time = time.time()
    time_in_bytes = struct.pack('>d', send_time)  # 把发出的时间,写入ICMP数据部分
    # 构建ICMP Echo数据包
    ping_one_reply = sr1(IP(dst=dst, ttl=ttl_ping) / ICMP(id=id_ping, seq=seq_ping) /\
                         time_in_bytes, timeout=2, verbose=False)
    try:
        if ping_one_reply.getlayer(ICMP).type == 0 and ping_one_reply.getlayer(
                ICMP).code == 0 and ping_one_reply.getlayer(ICMP).id == id_ping:  # 确认type,code和id是否匹配
            # 提取源IP,序列号,TTL,计算数据长度
            reply_source_ip = ping_one_reply.getlayer(IP).src
            reply_seq = ping_one_reply.getlayer(ICMP).seq
            reply_ttl = ping_one_reply.getlayer(IP).ttl
            reply_data_length = len(ping_one_reply.getlayer(Raw).load) + len(ping_one_reply.getlayer(Padding).load) + 8
            # 提取返回数据,转换为时间,并与当前时间计算时间差
            reply_data = ping_one_reply.getlayer(Raw).load
            receive_time = time.time()
            echo_request_sendtime = struct.unpack('>d', reply_data)
            time_to_pass_ms = (receive_time - echo_request_sendtime[0]) * 1000
            # 返回数据长度, 源IP地址,序列号,TTL和用时
            return reply_data_length, reply_source_ip, reply_seq, reply_ttl, time_to_pass_ms
    except Exception as e:
        if re.match('.*NoneType.*', str(e)):
            return None


def ping_result(dst):
    # 随机产生ICMP ID
    id_ping = random.randint(1, 65535)
    for i in range(1, 6):  # ping五个包
        ping_result = ping_one(dst, id_ping, i, 64)
        if ping_result:
            print('%d bytes from %s: icmp_seq=%d ttl=%d time=%4.0f ms' % (
                ping_result[0], ping_result[1], ping_result[2], ping_result[3], ping_result[4]))
            time.sleep(1)
        else:
            print('.', end='')


if __name__ == '__main__':
    # Windows Linux均可使用
    ping_result('192.168.98.129')
