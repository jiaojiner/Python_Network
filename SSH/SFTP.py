#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import paramiko, os, sys, time


def ssh_sftp_put(ip, user, password, local_file, remote_file, port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port, user, password)  # 连接服务器
    sftp = ssh.open_sftp()  # 打开sftp
    sftp.put(local_file, remote_file)  # 上传本地文件到服务器


def ssh_sftp_get(ip, user, password, remote_file, local_file, port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    ssh.connect(ip, port, user, password)  # 连接服务器
    sftp = ssh.open_sftp()  # 打开sftp
    sftp.get(remote_file, local_file)  # 下载服务器文件到本地


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    ssh_sftp_put('192.168.98.66', 'root', '1', 'Adv_SSH_Client.py', 'Adv_SSH_Client.py', port=22)
    # ssh_sftp_get('192.168.98.66', 'root', '1', 'nginx-1.9.9.tar.gz', 'nginx-1.9.9.tar.gz', port=22)
