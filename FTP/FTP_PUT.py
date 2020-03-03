#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import ftplib
import os


def putfile(hostname, file, username='anonymous', password='', rdir='.', ldir='.', verbose=True):
    if verbose: print('上传文件:', file)
    os.chdir(ldir)  # 切换本地工作目录
    local = open(file, 'rb')  # 读取本地文件
    remote = ftplib.FTP(hostname)  # 连接站点
    remote.encoding = 'GB18030'  # 使用中文编码
    remote.login(username, password)  # 输入用户名和密码进行登录
    remote.cwd(rdir)  # 切换FTP目录
    remote.storbinary('STOR ' + file, local, 1024)  # 上传文件
    remote.quit()  # 退出会话
    local.close()  # 关闭本地文件
    if verbose: print('上传文件:' + file + ' 结束！')


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    putfile('192.168.98.1', 'test.py', 'jiaojiner', 'w970210', rdir='/Python网络编程/FTP')
