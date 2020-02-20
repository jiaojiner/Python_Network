#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from Tools.minimumTFTP import Client


def ftpclient(server, filedir, file, operation=1):
    tftpClient = Client(server, filedir, file)
    if operation == 1:
        tftpClient.get()
    if operation == 2:
        tftpClient.put()
    print()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    # 正常安装有问题,需要把minimumTFTP.py文件放入如下的路径

    # ftpclient('192.168.98.29', '/root/python_network/TFTP', 'test.txt', operation=1)
    ftpclient('192.168.98.29', '/root/python_network/TFTP', '1.txt', operation=2)
