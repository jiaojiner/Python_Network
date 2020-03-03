#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


from Simple_SSH_Client import SSHClient_SingleCMD


def monitor_sshd(ip):
    username = 'root'
    password = 'root'
    result = SSHClient_SingleCMD(ip, username, password, 'systemctl status sshd')
    result_list = result.split('\n')
    for x in result_list:
        if x.split()[0] == 'Active:':
            #print(x)
            return x.split()[1] + x.split()[2]


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    print(monitor_sshd('192.168.98.66'))
