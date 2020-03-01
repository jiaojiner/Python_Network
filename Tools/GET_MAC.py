#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import os
import re  # 导入正则表达式模块


def get_mac_address(iface):  # 定义获取MAC地址的模块，传入接口名字
    # data = commands.getoutput("ifconfig " + iface)
    data = os.popen("ifconfig " + iface).read()  # 运行linux系统命令‘ifconifg’，并且读取输出信息赋值到data
    words = data.split()  # 把data中的数据通过空格分隔，并且产生清单
    found = 0  # 是否找到MAC地址
    location = 0  # 搜索清单的位置记录
    index = 0  # MAC地址所在清单中的位置
    for x in words:  # 遍历整个清单
        if re.match('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', x):  # 匹配MAC地址字段
            found = 1  # MAC地址被找到
            index = location  # 记录MAC地址出现的位置
            break  # 跳出循环
        else:  # 如果没有匹配MAC地址字段
            location = location + 1  # 继续执行循环，收索下一个位置，所以location需要加1
    if found == 1:  # 如果MAC地址被找到
        mac = words[index]  # 提取清单中MAC地址（通过记录的位置），并且赋值到mac
    else:  # 如果没有找到MAC地址
        mac = 'Mac not found'  # 返回MAC地址没找到的信息
    return mac  # 返回mac


if __name__ == "__main__":
    print(get_mac_address('ens33'))


# def get_mac(ifname):
#     ifconfig_result = (os.popen('ifconfig ' + ifname).read()).split('\n')
#     # print(ifconfig_result)
#     for ip in ifconfig_result:
#         if re.findall('(\w{1,2}\:\w{1,2}\:\w{1,2}\:\w{1,2}\:\w{1,2}\:\w{1,2})',ip):
#             re_result = re.findall('(\w{1,2}\:\w{1,2}\:\w{1,2}\:\w{1,2}\:\w{1,2}\:\w{1,2})',ip)
#             for mac in re_result:
#                 return str(mac)
#             break
#     else:
#         return None
#
#
# if __name__ == '__main__':
#     mac_result = get_mac('ens33')
#     print(mac_result)
