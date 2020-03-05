#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from Tools.minimumTFTP import Server


def tftpserver(dir):
    print("TFTP服务器准备就绪,根目录为", dir)
    ftpServer = Server(dir)
    ftpServer.run()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    # 正常安装有问题,需要的minimumTFTP.py在Tools目录下
    tftpserver('/root/python_network/TFTP/tftp_test')
