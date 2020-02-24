#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import time
from Tools.GET_IP_netifaces import get_ip_address
from socket import *


def tcp_server(ifname='ens33', local_port='8888'):
    local_ip = get_ip_address(ifname)
    tcp_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP Socket, AF_INET为IPv4，SOCK_STREAM为TCP
    tcp_socket.bind((local_ip, local_port))  # 绑定套接字到地址，地址为（host，port）的元组
    tcp_socket.listen(5)  # 在拒绝连接前，操作系统可以挂起的最大连接数量，一般配置为5
    try:
        while True:  # 一直接受请求，直到ctl+c终止程序
            # 接受TCP连接，并且返回（conn,address）的元组，conn为新的套接字对象，可以用来接收和发送数据，address是连接客户端的地址
            connection, address = tcp_socket.accept()
            # 打印连接客户端的IP地址
            print('Server Connected by', address)
            while True:
                data = connection.recv(1024)  # 接收数据，1024为bufsize，表示一次接收的最大数据量！
                if not data: break  # 如果没有数据就退出循环
                connection.send(b'Echo==>' + data)  # 发送回显数据给客户，注意Python3.x后，发送和接收的数据必须为二进制！
            connection.close()  # 关闭连接
    except KeyboardInterrupt:
        time.sleep(1)
        print('用户手动退出服务端')


if __name__ == "__main__":
    server_ip = input('请输入需要监听的接口名称：')
    server_port = int(input('请输入需要监听的端口号：'))
    tcp_server(server_ip, server_port)
