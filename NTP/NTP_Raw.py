#!/usr/bin/env python3
# # -*- encoding = utf-8 -*-
# # 该代码由本人学习时编写，仅供自娱自乐！
# # 本人QQ：1945962391
# # 欢迎留言讨论，共同学习进步！


import socket
import struct
import time

TIME_1970 = 2208988800


def ntp_client(ntp_server):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket.AF_INET为IP，socket.SOCK_DGRAM为UDP
    data = b'\x1b' + 47 * b'\0'  # \x1b(00 011(版本3) 011(客户模式)) + 47个\0凑齐48个字节的头部
    client.sendto(data, (ntp_server, 123))  # 数据，IP地址和端口号
    data, address = client.recvfrom(1024)  # 接收缓存为1024
    if data:
        print('Response received from:', address)  # 如果收到数据，打印地址信息
    # print(data)
    s = struct.unpack('!12I', data)  # 48个字节，12个四字节
    print(s)
    t = struct.unpack('!12I', data)[-2]  # 倒数第二个为时间
    print(t)
    t -= TIME_1970  # Linux 自己的系统时间，由 1970/01/01 开始计时的时间参数
    # print(t)
    print('\tTime=%s' % time.ctime(t))


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    ntp_client("ntp.aliyun.com")
