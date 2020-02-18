#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

from multiprocessing.pool import ThreadPool
from ARP.APR_Request import arp_request
import ipaddress
from Tools.SORT_IP import sort_ip

nets_list = []


def arp_scan(nets,ifname):
    net = ipaddress.ip_network(nets)
    for ip in net:
        nets_list.append(str(ip))
    # for i in nets_list:
    # result = []
    #     result.append(arp_request(i, ifname))
    # print(result[-1][0])
    pool = ThreadPool(processes=100)
    result = []
    for i in nets_list:
        result.append(pool.apply_async(arp_request, args=(i, ifname)))
    pool.close()
    pool.join()
    # print(result[0].get())
    scan_result = []
    for ip_exit in result:
        if ip_exit.get()[-1] == None:
            continue
        scan_result.append(ip_exit.get()[0])
    return sort_ip(scan_result)


if __name__ == '__main__':
    result = arp_scan('192.168.98.0/30', 'ens33')
    print(result)
