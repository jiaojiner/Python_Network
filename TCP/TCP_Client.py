#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！


import time
from socket import *


def tcp_server(localip, local_port):
    tcp_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP Socket, AF_INET为IPv4，SOCK_STREAM为TCP
    tcp_socket.connect((localip, local_port))  # 绑定套接字到地址，地址为（host，port）的元组
    try:
        while True:  # 一直接受请求，直到ctl+c终止程序
            msg = input("请输入回显信息(exit退出):")
            if msg == "":
                print("请输入正确信息!!!")
            elif msg != 'exit':
                tcp_socket.send(msg.encode())
                echo_msg = tcp_socket.recv(1024)
                print(echo_msg.decode())
            else:
                break
        tcp_socket.close()
        print("连接已经结束！！！")
    except KeyboardInterrupt:
        time.sleep(1)
        print('用户手动退出')


if __name__ == "__main__":
    server_ip = input('请输入需要连接的服务器地址：')
    server_port = int(input('请输入需要连接的端口号：'))
    tcp_server(server_ip, server_port)
