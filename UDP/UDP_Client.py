#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import socket
import sys
import time

server_ip = input('请输入需要连接UDP服务端的IP地址:')
server_port = input('请输入需要连接UDP服务端的端口号:')
ipaddress = (server_ip, int(server_port))  # 设置需要连接的服务端地址与端口
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建udp连接
udp_socket.connect(ipaddress)  # 连接服务端

while True:
    try:
        data = input('请输入需要传输的数据：')
        if not data:  # 如果无数据输入，发送空数据，并退出循环
            udp_socket.sendto(data.encode(), ipaddress)  # 需将数据编码发送
            print('无数据输入，程序即将退出！')
            time.sleep(1)
            break
        else:  # 否则传输数据，继续循环
            udp_socket.sendto(data.encode(), ipaddress)
            print('数据传输完毕！')
    except KeyboardInterrupt:  # 如客户输入ctrl+c，打印提示信息，退出程序
        print('用户手动退出程序！')
        sys.exit()
udp_socket.close()
