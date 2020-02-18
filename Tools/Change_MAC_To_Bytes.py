#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import struct
import re


def Change_MAC_To_Bytes(mac):
    # 去除各种MAC地址的分隔符
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    # 通过移位操作,得到MAC地址的6个字节
    section1 = mac_value >> 40 & 0xff
    section2 = mac_value >> 32 & 0xff
    section3 = mac_value >> 24 & 0xff
    section4 = mac_value >> 16 & 0xff
    section5 = mac_value >> 8 & 0xff
    section6 = mac_value & 0xff
    # 拼接MAC地址的6个字节,返回转换为字节的MAC地址
    Bytes_MAC = struct.pack('!6B', section1, section2, section3, section4, section5, section6)
    return Bytes_MAC


if __name__ == "__main__":
    print(Change_MAC_To_Bytes("00:50:56:AB:25:08"))
