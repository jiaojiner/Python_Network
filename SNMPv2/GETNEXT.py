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


from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmpv2_getnext(ip, community, oid, port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData(community),  # 设置community
        cmdgen.UdpTransportTarget((ip, port)),  # 设置IP地址和端口号
        oid,  # 设置OID
    )
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBindTable[int(errorindex) - 1][0] or '?'
        )
              )

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for varBindTableRow in varBindTable:
        for item in varBindTableRow:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 显示接口信息
    print(snmpv2_getnext("192.168.98.130", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161))
    for x, y in snmpv2_getnext("192.168.98.130", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161):
        print(x, y)
    # 接口速率
    print(snmpv2_getnext("192.168.98.130", "tcpipro", "1.3.6.1.2.1.2.2.1.5", port=161))

    # 进接口字节数
    print(snmpv2_getnext("192.168.98.130", "tcpipro", "1.3.6.1.2.1.2.2.1.10", port=161))

    # 出接口字节数
    print(snmpv2_getnext("192.168.98.130", "tcpipro", "1.3.6.1.2.1.2.2.1.16", port=161))
