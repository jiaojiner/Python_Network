#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import struct
import re


def Change_IP_To_Bytes(IP):
    section1 = int(IP.split('.')[0])
    section2 = int(IP.split('.')[1])
    section3 = int(IP.split('.')[2])
    section4 = int(IP.split('.')[3])
    Bytes_IP = struct.pack('>4B', section1, section2, section3, section4)

    return Bytes_IP


if __name__ == "__main__":
    print(Change_IP_To_Bytes("10.1.1.80"))