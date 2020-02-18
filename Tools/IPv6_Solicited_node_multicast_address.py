#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


def full_ipv6(ipv6):  # 转换为完整的IPv6地址
    ipv6_section = ipv6.split(":")  # 对原始地址使用":"进行分割

    ipv6_section_len = len(ipv6.split(":"))  # 了解原始地址的分段数量

    null_location = ipv6_section.index('')  # 找到空位,这个地方要补0

    ipv6_section.pop(null_location)  # 把原来的空位弹出去

    add_section = 8 - ipv6_section_len + 1  # 计算需要补"0000"的个数

    for x in range(add_section):
        ipv6_section.insert(null_location, "0000")  # 开始补"0000"

    new_ipv6 = []
    for s in ipv6_section:
        if len(s) < 4:
            new_ipv6.append((4 - len(s)) * '0' + s)  # 对于不够长度的左边补"0"
        else:
            new_ipv6.append(s)
    return ':'.join(new_ipv6)  # 使用":"连接在一起成为完整的IPv6地址


def Solicited_node_multicast_address(ipv6):
    return "FF02::1:FF" + full_ipv6(ipv6)[-7:]  # 拼接得到Solicited_node_multicast_address


if __name__ == '__main__':
    print(full_ipv6("FF02::1:FF00:200"))
    print(full_ipv6("2001:1::200"))
    print(Solicited_node_multicast_address("2001:1::200"))
