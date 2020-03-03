#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


from telnetlib import Telnet
# import re  # 可以使用正则表达式匹配回显，然后做判断，决定下一步的操作
import time


def TelnetClient(ip, username, password, cmd_list, enable='csr', verbose=True):
    tn = Telnet(ip, 23)
    # print(tn.expect([], timeout=1))
    # print(tn.expect([], timeout=1)[2])
    # print(tn.expect([], timeout=1)[2].decode())
    # print(tn.expect([], timeout=1)[2].decode().strip())
    rackreply = tn.expect([], timeout=1)[2].decode().strip()  # 读取回显
    if verbose:
        print(rackreply)  # 打印回显
    tn.write(username.encode())  # 任何字串都需要转成二进制字串
    tn.write(b'\n')  # 注意一定要打回车
    time.sleep(1)  # 在命令之间留出一定的时间间隔！否则路由器可能反应不过来
    rackreply = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreply)  # 打印回显
    tn.write(password.encode())
    tn.write(b'\n')
    time.sleep(1)
    rackreply = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreply)  # 打印回显
    if enable is not None:
        tn.write(b'enable\n')
        time.sleep(1)
        rackreply = tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rackreply)  # 打印回显
        tn.write(enable.encode())
        tn.write(b'\n')
        rackreply = tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rackreply)  # 打印回显
    time.sleep(1)
    for cmd in cmd_list:  # 读取命令，并且逐个执行！
        tn.write(cmd.encode() + b'\n')
        rackreply = tn.expect([], timeout=1)[2].decode().strip()
        if verbose:
            print(rackreply)  # 打印回显
        time.sleep(1)
    tn.write(b'exit\n')
    rackreply = tn.expect([], timeout=1)[2].decode().strip()
    if verbose:
        print(rackreply)  # 打印回显
    tn.close()


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    cmds = ['terminal length 0', 'show ver', 'config ter', 'router ospf 1']
    TelnetClient('192.168.98.130', 'csr', 'csr', cmd_list=cmds, verbose=True)
