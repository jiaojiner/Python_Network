#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391
# 欢迎留言讨论，共同学习进步！

import socket


class Facility:
    # Syslog facilities
    KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP = range(12)
    LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7 = range(16, 24)


class Level:
    # Syslog levels
    EMERG, ALERT, CRIT, ERR, WARNING, NOTICE, INFO, DEBUG = range(8)


class Syslog:
    # A syslog client that logs to a remote server.
    def __init__(self, host="localhost", port=514, facility=Facility.LOCAL7):
        self.host = host
        self.port = port
        self.facility = facility
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message, level):
        # Send a syslog message to remote host using UDP.
        data = "<%d>%s" % (level + self.facility * 8, message)
        self.socket.sendto(data.encode(), (self.host, self.port))

    def warn(self, message):
        # Send a syslog warning message.
        self.send(message, Level.WARNING)

    def notice(self, message):
        # Send a syslog notice message.
        self.send(message, Level.NOTICE)

    def error(self, message):
        # Send a syslog error message.
        self.send(message, Level.ERR)


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    log = Syslog("192.168.98.29")
    log.send("syslog test", Level.NOTICE)
