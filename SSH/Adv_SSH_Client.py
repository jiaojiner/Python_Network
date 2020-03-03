#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import paramiko
import time
import sys


def SSHClient_MultiCMD(ip, username, password, cmd_list, enable_password='csr', verbose=True):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # SSH连接

    chan = ssh.invoke_shell()  # 激活交互式shell
    time.sleep(1)
    x = chan.recv(2048).decode()  # 接收回显信息
    for cmd in cmd_list:  # 读取命令
        chan.send(cmd.encode())  # 执行命令，注意字串都需要编码为二进制字串
        chan.send(b'\n')  # 一定要注意输入回车
        time.sleep(2)  # 由于有些回显可能过长，所以可以考虑等待更长一些时间
        x = chan.recv(40960).decode()  # 读取回显，有些回想可能过长，请把接收缓存调大
        if verbose:
            print(x)  # 打印回显

    chan.close()  # 退出交互式shell
    ssh.close()  # 退出ssh会话


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    SSHClient_MultiCMD('192.168.98.130', 'csr', 'csr', ['terminal length 0', 'show ver', 'config ter', 'router ospf 1'])
    # SSHClient_MultiCMD('192.168.98.66', 'root', '1', ['ifconfig', 'df -h', 'free -m'])
