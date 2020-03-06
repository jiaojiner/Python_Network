#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

""" snmp v2c 配置
snmp-server community tcpipro RO
snmp-server community tcpiprw RW
snmp-server location neimenggu
snmp-server contact NULL
snmp-server enable traps snmp linkdown linkup
snmp-server host 192.168.98.29 version 2c csr
snmp-server host 192.168.98.30 version 2c csr
"""

import sqlite3
from dateutil import parser


def cpu_show(dbname):
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 提取时间与CPU利用率信息
    cursor.execute("select time, cpu from routerdb")
    yourresults = cursor.fetchall()

    time_list = []
    cpu_list = []

    # 把结果写入time_list和cpu_list的列表
    for time_cpu in yourresults:
        time_list.append(time_cpu [0])
        cpu_list.append(time_cpu[1])

    # 转换字符串到时间对象
    time_list = [parser.parse(i) for i in time_list]

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdate
    import matplotlib.ticker as mtick

    f, ax = plt.subplots(1)

    # 格式化X轴
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S"))  # 设置时间标签显示格式
    # 格式化Y轴
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))#格式化Y轴
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))  # 格式化Y轴
    # 传入数据,time为X轴,cpu为Y轴
    ax.plot(time_list, cpu_list)
    # 设置Y轴 最小值和最大值
    ax.set_ylim(ymin=0, ymax=100)
    # 显示图像
    plt.show()


def mem_show(dbname):
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 提取时间,MEM使用量和空闲量
    cursor.execute("select time, memu, memf from routerdb")
    yourresults = cursor.fetchall()

    time_list = []
    mem_list = []

    # 把结果写入time_list和cpu_list的列表
    for time_mem in yourresults:
        time_list.append(time_mem[0])

        mem_list.append((time_mem[1]/(time_mem[1] + time_mem[2]))*100)

    # 转换字符串到时间对象
    time_list = [parser.parse(i) for i in time_list]

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdate
    import matplotlib.ticker as mtick

    f, ax = plt.subplots(1)

    # 格式化X轴
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S"))  # 设置时间标签显示格式
    # 格式化Y轴
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))#格式化Y轴
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))  # 格式化Y轴
    # 传入数据,time为X轴,cpu为Y轴
    ax.plot(time_list, mem_list)
    # 设置Y轴 最小值 和 最大值
    ax.set_ylim(ymin=0, ymax=100)
    # 显示图像
    plt.show()


if __name__ == '__main__':
    cpu_show("deviceinfo.sqlite")
    # mem_show("deviceinfo.sqlite")
