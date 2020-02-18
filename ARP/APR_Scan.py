#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from multiprocessing.pool import ThreadPool
from ARP.APR_Request import arp_request
import ipaddress
from Tools.SORT_IP import sort_ip

nets_list = []  # 创建存放ip地址的空列表


def arp_scan(nets, ifname):  # 定义扫描方法
    net = ipaddress.ip_network(nets)  # 通过ipaddress模块将输入的网段转换成对象
    for ip in net:  # 通过for循环将网段中的所有ip地址提取后转换为字符串，存在到net_list列表中
        nets_list.append(str(ip))
    # for i in nets_list:
    # result = []
    #     result.append(arp_request(i, ifname))
    # print(result[-1][0])
    pool = ThreadPool(processes=100)  # 创建多进程资源池，设定100个进程同时启动
    result = []  # 定义进程返回结果存放的空列表
    for i in nets_list:  # 使用for循环将之前存放ip地址的列表中的地址逐个提取并作为参数传入到arp_request函数中
        result.append(pool.apply_async(arp_request, args=(i, ifname)))
    pool.close()  # 关闭进程资源池
    pool.join()  # 等待所有进程完成
    # print(result[0].get())
    scan_result = []  # 定义提取进程返回值的空列表
    for ip_exit in result:  # 循环读取返回值，需使用get方法将进程返回参数转换为正常函数返回格式
        if ip_exit.get()[-1] == None:  # 判断arp_request返回结果中最后一位是否存在数据，如果不存在，直接下次循环
            continue
        scan_result.append(ip_exit.get()[0])  # 如果存在，提取返回值中的ip地址，放于scan_result列表中
    return sort_ip(scan_result)  # 通过sort_ip函数对返回的ip地址进行排序，并返回


if __name__ == '__main__':
    result = arp_scan('192.168.98.0/24', 'ens33')
    for scan_result in result:
        print(scan_result)  # 循环打印返回列表中的ip地址
