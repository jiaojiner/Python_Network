#!/usr/bin/env python3
# coding:gbk

import socket
import select

# import select
# select 在windows下只能监控socket
# 在Linux下可以监控所有i/o
# stdin,stdout,stderr = select.select(rlist,wlist,xlist,[timeout])
# rlist 监控的准备读的东西
# wlist 监控的准备写的东西
# xlist 监控错误

# stdin 如果读的东西发生变化赋值
# stdout 如果写的东西发生变化赋值
# stderr 如果发生错误赋值
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化socket对象
sock.setblocking(False)  # 设置为非阻塞式socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 假如端口被socket使用过，
# 并且利用socket.close()来关闭连接，
# 但此时端口还没有释放，
# 要经过一个TIME_WAIT的过程之后才能使用，
# 为了实现端口的马上复用，
# 可以选择setsockopt()函数来达到目的。
sock.bind(("", 8000))  # 服务端绑定ip,端口
sock.listen(5)  # 监听端口
inputs = [sock]  # 实例化一个列表，将sock放入列表当中
outputs = []  # 实例化一个空列表
errputs = []  # 实例化一个空列表

while True:
    # 设置监听的对象，并且返回三个参数
    stdin, stdout, stderr = select.select(inputs, outputs, errputs, 1)
    # print(stdin, stdout, stderr)
    if stdin:  # 如果输出有东西，也就是准备要读的内容有变化，返回了值
        for s in stdin:  # 返回值为列表
            # 元素有可能是sock对象
            print(stdin)  # 打印
            if s is sock:  # 判断返回的是sock对象本身吗
                con, add = s.accept()  # 如果是，接受数据
                print("%s:%s is connectd" % add)  # 打印请求者身份
                inputs.append(con)  # 把con放入inputs

            else:  # 如果不是sock对象本身 s 如果不是sock就是con
                data = s.recv(512)  # 接受数据
                if not data:  # 如果数据为空
                    inputs.remove(s)  # 从列表当中删除s对象
                else:
                    print(data)  # 打印接收的数据
