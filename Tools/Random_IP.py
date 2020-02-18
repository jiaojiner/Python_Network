#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！


import random


def Random_Section():
    section = random.randint(1, 254)
    return section


def Random_IP():
    IP = str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section())
    return IP


if __name__ == '__main__':
    print(Random_IP())
