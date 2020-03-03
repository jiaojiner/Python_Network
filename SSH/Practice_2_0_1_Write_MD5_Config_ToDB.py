#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import os
import sqlite3
from Practice_2_Get_MD5_Config import get_md5_config
import datetime
import time


def createdb(dbname):
    if os.path.exists(dbname):
        os.remove(dbname)
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 创建数据库

    cursor.execute("create table configdb(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                                         time varchar(64), \
                                         device_ip varchar(32),\
                                         md5_value varchar(32),\
                                         config varchar(40960)\
                                         )")
    conn.commit()


def writedb(time, device_ip, md5_value, config, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("insert into configdb (time, \
                                          device_ip, \
                                          md5_value, \
                                          config) values ('%s', '%s', '%s', '%s')" % (time,
                                                                                            device_ip,
                                                                                            md5_value,
                                                                                            config))
    conn.commit()


def get_config_writedb(host, username, password, dbname, seconds):
    while seconds >= 0:
        result = get_md5_config(host, username, password, operation=0)
        config = result[host][0]
        md5_value = result[host][1]
        writedb(datetime.datetime.now(), host, md5_value, config, dbname)
        time.sleep(5)
        seconds -= 5


if __name__ == '__main__':
    createdb('configdb.sqlite')
    get_config_writedb('192.168.98.129', 'root', 'root', 'configdb.sqlite', 60)
