#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from Tools import GET_IP_netifaces
import socket
import sys
import time

localnets = input('请输入需要监听的网卡名称：')
localport = input('请输入需要监听的端口：')  # input传入的数据类型为string
localip = GET_IP_netifaces.get_ip_address(localnets)
ipadress = (localip, int(localport))
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建udp的socket套接字
udp_socket.bind(ipadress)  # 绑定ip地址及端口

print('Server端已准备就绪！等待数据传输')

while True:
    try:
        data, ipaddr = udp_socket.recvfrom(2048)
        # print(udp_socket.recvfrom(2048))
        if not data:
            print('客户端程序已退出！服务端即将断开')
            time.sleep(1)
            break
        print('接收来自', ipaddr, '的数据！', '传输内容为：', data)
    except KeyboardInterrupt:
        print('服务端准备退出！')
        time.sleep(1)
        sys.exit()
udp_socket.close()
