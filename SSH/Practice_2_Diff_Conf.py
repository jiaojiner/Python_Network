#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


from difflib import *


def diff_file(file1, file2):
    txt1 = open(file1, 'r').readlines()
    txt2 = open(file2, 'r').readlines()
    result = Differ().compare(txt1, txt2)
    return_result = '\n'.join(list(result))
    return return_result


def diff_txt(txt1, txt2):
    txt1_list = txt1.split('\r\n')
    txt2_list = txt2.split('\r\n')
    result = Differ().compare(txt1_list, txt2_list)
    return_result = '\r\n'.join(list(result))
    return return_result


if __name__ == '__main__':
    txt1 = '''\r\nBuilding configuration...\r\n\r\nCurrent configuration : 2406 bytes
            \r\n!\r\nversion 15.2\r\nservice timestamps debug datetime msec'''
    txt2 = '''\r\nBuilding configur...\r\n\r\nCurrent configuran : 2407 bytes
            \r\n!\r\nversion 15.2\r\nservice timestamps debug datetime msec'''
    # print(diff_txt(txt1, txt2))
    print(diff_file('txt1.txt', 'txt2.txt'))

