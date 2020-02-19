#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import ipaddress
from multiprocessing.pool import ThreadPool
from ICMP与IPv6.Ping_one import ping_one
from Tools.SORT_IP import sort_ip


# def ping_scan(nets):
#     ip_result = ipaddress.ip_network(nets)
#     ip_list = []
#     for ip in ip_result:
#         ip_list.append(str(ip))
#     pool = ThreadPool(processes=10)  # 创建多进程资源池，设定100个进程同时启动
#     result = []  # 定义进程返回结果存放的空列表
#     result.append(pool.map(ping_one, ip_list))
#     pool.close()  # 关闭进程资源池
#     pool.join()  # 等待所有进程完成
#     # print(result)
#     # pool1 = result.pop()
#     # print(type(pool1))
#     # print(result.get()[-1])
#     scan_result = []  # 定义提取进程返回值的空列表
#     for ip_exit in result:  # 循环读取返回值，需使用get方法将进程返回参数转换为正常函数返回格式
#         for ip_1 in ip_exit:
#             if ip_1[-1] == 2:  # 判断arp_request返回结果中最后一位是否存在数据，如果不存在，直接下次循环
#                 continue
#             scan_result.append(ip_1[0])  # 如果存在，提取返回值中的ip地址，放于scan_result列表中
#     return sort_ip(scan_result)  # 通过sort_ip函数对返回的ip地址进行排序，并返回


# def ping_scan(nets):
#     ip_result = ipaddress.ip_network(nets)
#     ip_list = []
#     for ip in ip_result:
#         ip_list.append(str(ip))
#     pool = ThreadPool(processes=10)  # 创建多进程资源池，设定100个进程同时启动
#     result = {}  # 定义进程返回结果存放的空列表
#     for i in ip_list:  # 使用for循环将之前存放ip地址的列表中的地址逐个提取并作为参数传入到arp_request函数中
#         result_1 = pool.apply_async(ping_one, args=(i,))
#         result[str(ip)] = result_1
#     pool.close()  # 关闭进程资源池
#     pool.join()  # 等待所有进程完成
#     # print(result)
#     # pool1 = result.pop()
#     # print(type(pool1))
#     # print(result.get()[-1])
#     scan_result = []  # 定义提取进程返回值的空列表
#     for ip_key, ip_value in result.items():  # 循环读取返回值，需使用get方法将进程返回参数转换为正常函数返回格式
#         if ip_value.get()[-1] == 1:  # 判断arp_request返回结果中最后一位是否存在数据，如果不存在，直接下次循环
#             scan_result.append(ip_key)  # 如果存在，提取返回值中的ip地址，放于scan_result列表中
#     return sort_ip(scan_result)  # 通过sort_ip函数对返回的ip地址进行排序，并返回


def ping_scan(nets):
    ip_result = ipaddress.ip_network(nets)
    ip_list = []
    for ip in ip_result:
        ip_list.append(str(ip))
    pool = ThreadPool(processes=100)  # 创建多进程资源池，设定100个进程同时启动
    result = []  # 定义进程返回结果存放的空列表
    for i in ip_list:  # 使用for循环将之前存放ip地址的列表中的地址逐个提取并作为参数传入到arp_request函数中
        result.append(pool.apply_async(ping_one, args=(i,)))
    pool.close()  # 关闭进程资源池
    pool.join()  # 等待所有进程完成
    # print(result)
    # ip1 = result[0].get()
    # print(ip1)
    # print(type(result))
    # pool1 = result.pop()
    # print(type(pool1))
    # print(result.get()[-1])
    scan_result = []  # 定义提取进程返回值的空列表
    for ip_exit in result:  # 循环读取返回值，需使用get方法将进程返回参数转换为正常函数返回格式
        if ip_exit.get()[-1] == 2:  # 判断arp_request返回结果中最后一位是否存在数据，如果不存在，直接下次循环
            continue
        scan_result.append(ip_exit.get()[0])  # 如果存在，提取返回值中的ip地址，放于scan_result列表中
    return sort_ip(scan_result)  # 通过sort_ip函数对返回的ip地址进行排序，并返回


if __name__ == '__main__':
    scan_result = ping_scan('192.168.98.0/24')
    if scan_result:
        print('该网段活动主机如下：')
        for ip in scan_result:
            print(ip)
    else:
        print('该网段暂无活动主机！')
