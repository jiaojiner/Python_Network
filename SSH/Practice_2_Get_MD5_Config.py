#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


from Simple_SSH_Client import SSHClient_SingleCMD
import re


def get_md5_config(host, username, password, operation=0):
    dict_config = {}
    if operation == 0:  # 如果操作码为0，表示MD5和Config都要获取！
        try:
            # 获取完整的running-configuration
            run_config = SSHClient_SingleCMD(host, username, password, 'show run')
            # 下面部分在做running-configuration的裁剪操作，只留hostname开始的配置
            list_run_config = run_config.split('\r\n')
            location = 0
            host_location = 0
            for i in list_run_config:
                if re.match('.*hostname .*', i):
                    host_location = location  # 定位hostname所在位置
                else:
                    location += 1
            list_run_config = list_run_config[host_location:]  # 截取hostname开始往后的部分
            run_config = '\r\n'.join(list_run_config)  # 再次还原为字串形式的配置
            # 获取配置的md5值
            md5 = SSHClient_SingleCMD(host, username, password, 'verify /md5 system:running-config')
            dict_config[host] = [run_config, md5.strip()[-32:]]
        # 仅仅截取最后32位的MD5值
        # 返回字典
        except Exception as e:
            print('%stErrorn %s' % (host, e))
    elif operation == 1:  # 如果操作码为1，表示只获取Config！
        try:
            run_config = SSHClient_SingleCMD(host, username, password, 'show run')
            list_run_config = run_config.split('\r\n')
            location = 0
            host_location = 0
            for i in list_run_config:
                if re.match('.*hostname .*', i):
                    host_location = location
                else:
                    location += 1
            list_run_config = list_run_config[host_location:]
            run_config = '\r\n'.join(list_run_config)
            dict_config[host] = run_config
        except Exception as e:
            print('%stErrorn %s' % (host, e))
    elif operation == 2:  # 如果操作码为1，表示只获取MD5值！
        try:
            md5 = SSHClient_SingleCMD(host, username, password, 'verify /md5 system:running-config')
            dict_config[host] = md5.strip()[-32:]
        except Exception as e:
            print('%stErrorn %s' % (host, e))
    else:
        print('操作码传入错误！')
    return dict_config


if __name__ == '__main__':
    print(get_md5_config('192.168.98.129', 'root', 'root', operation=1))
