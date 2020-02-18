#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import struct


def Change_Chaddr_To_MAC(chaddr):  # 转换16字节chaddr为MAC地址，前6字节为MAC，后面暂时无用！！
    MAC_ADDR_INT_List = struct.unpack('>16B', chaddr)[:6]
    MAC_ADDR_List = []
    for MAC_ADDR_INT in MAC_ADDR_INT_List:
        if MAC_ADDR_INT < 16:
            MAC_ADDR_List.append('0' + str(hex(MAC_ADDR_INT))[2:])
        else:
            MAC_ADDR_List.append(str(hex(MAC_ADDR_INT))[2:])
    MAC_ADDR = MAC_ADDR_List[0] + ':' + MAC_ADDR_List[1] + ':' + MAC_ADDR_List[2] + ':' + MAC_ADDR_List[3] + ':' + \
               MAC_ADDR_List[4] + ':' + MAC_ADDR_List[5]
    return MAC_ADDR
