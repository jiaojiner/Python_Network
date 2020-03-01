#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import os
import re  # 导入正则表达式模块


# def get_ip_address_ifconfig(iface):  # 定义获取网络地址的模块，传入接口名字
#     # data = commands.getoutput("ifconfig " + iface)
#     data = os.popen("ifconfig " + iface).read()  # 运行linux系统命令‘ifconifg’，并且读取输出信息赋值到data
#     words = data.split()  # 把data中的数据通过空格分隔，并且产生清单
#     # print(words)
#
#     ip_found = 0  # 是否找到IP地址
#     network_found = 0  # 是否找到网络地址
#     broadcast_found = 0  # 是否找到广播地址
#     location = 0  # 搜索清单的位置记录
#     ip_index = 0  # IP地址所在清单中的位置
#     network_index = 0  # 网络地址所在清单中的位置
#     broadcast_index = 0  # 广播地址所在清单中的位置
#
#     for x in words:  # 遍历整个清单
#         # print(x)
#         if re.findall('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', x):  # 匹配地址字段
#             result = re.findall('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', x)  # 匹配的结果赋值给result
#             # print(result)
#             if result[0][3] == '0':  # 最后一个字段为0，即为网络地址
#                 network_found = 1  # 网络地址被找到
#                 network_index = location  # 记录网络地址出现的位置
#                 location = location + 1  # 继续执行循环，收索下一个位置，所以location需要加1
#             elif result[0][3] == '255':  # 最后一个字段为255，即为广播地址
#                 broadcast_found = 1  # 广播地址被找到
#                 broadcast_index = location  # 记录广播地址出现的位置
#                 location = location + 1  # 继续执行循环，收索下一个位置，所以location需要加1
#             else:  # 最后一个字段非0和255，即为IP地址
#                 ip_found = 1  # IP地址被找到
#                 ip_index = location  # 记录IP地址出现的位置
#                 # print(ip_index)
#                 location = location + 1  # 继续执行循环，收索下一个位置，所以location需要加1
#         else:  # 如果没有匹配地址字段
#             location = location + 1  # 继续执行循环，收索下一个位置，所以location需要加1
#     if ip_found == 1:  # 如果IP地址被找到
#         ip = words[ip_index]  # 提取清单中IP地址（通过记录的位置），并且赋值到IP
#     else:
#         ip = None  # 如果没有找到返回None
#
#     if network_found == 1:  # 如果网络地址被找到
#         network = words[network_index]  # 提取清单中网络地址（通过记录的位置），并且赋值到IP
#     else:
#         network = None  # 如果没有找到返回None
#
#     if broadcast_found == 1:  # 如果广播地址被找到
#         broadcast = words[broadcast_index]  # 提取清单中广播地址（通过记录的位置），并且赋值到IP
#     else:
#         broadcast = None  # 如果没有找到返回None
#
#     get_ip_address_result = {'ip_address': ip, 'network_mask': network,
#                              'broadcast_address': broadcast}  # 创建包括IP，网络和广播地址的字典
#     return get_ip_address_result  # 返回包括IP，网络和广播地址的字典内容
#
#
# if __name__ == "__main__":
#     for x, y in get_ip_address_ifconfig('ens33').items():
#         print(x, y)


def get_ip(ifname):
    ifconfig_result = (os.popen('ifconfig ' + ifname).read()).split('\n')
    # print(ifconfig_result)
    for ip in ifconfig_result:
        if re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ip):
            re_result = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ip)
            for ip in re_result:
                if ip.split('.')[-1] == '0':
                    mask = ip
                elif ip.split('.')[-1] == '255':
                    network = ip
                else:
                    ipv4 = ip
    return mask, network, ipv4


if __name__ == '__main__':
    ip_result = get_ip('ens33')
    print('子网掩码为：', ip_result[0])
    print('子网广播为：', ip_result[1])
    print('IP地址为：', ip_result[2])
