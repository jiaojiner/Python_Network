#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import random


def hex():
    hex_mac = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'e', 'f'])
    return str(hex_mac)


def Random_MAC():
    MAC = hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex() + ':' + hex() + hex()
    return MAC


if __name__ == '__main__':
    print(Random_MAC())
