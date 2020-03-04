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
from pysnmp.proto import rfc1902


def snmpv2_set(ip, community, oid, value, port=161):
    cmdGen = cmdgen.CommandGenerator()
    # print(dir(rfc1902))
    # 类型 ['ApplicationSyntax', 'Bits', 'Counter32', 'Counter64', 'Gauge32',
    # 'Integer', 'Integer32', 'IpAddress', 'ObjectIdentifier', 'ObjectName',
    # 'ObjectSyntax', 'OctetString', 'Opaque', 'SimpleSyntax', 'TimeTicks',
    # 'Unsigned32', '__all__', '__builtins__', '__cached__', '__doc__',
    # '__file__', '__loader__', '__name__', '__package__', '__spec__',
    # 'constraint', 'error', 'namedtype', 'namedval', 'rfc1155', 'tag', 'univ', 'version_info']
    # 需要提前通过OIDVIEW查询类型
    # 通过不同的类型写入数据
    if isinstance(value, str):
        set_value = rfc1902.OctetString(value)
    elif isinstance(value, int):
        set_value = rfc1902.Integer(value)

    errorIndication, errorStatus, errorindex, varBinds = cmdGen.setCmd(
        cmdgen.CommunityData(community),  # 写入Community
        cmdgen.UdpTransportTarget((ip, port)),  # IP地址和端口号
                                  (oid, set_value)  # OID和写入的内容，需要进行编码！
        )
    # 错误处理
    if errorIndication:
        print("写入错误!!!")
        print(errorIndication)
    elif errorStatus:
        print("写入错误!!!")
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )
    else:
        print("写入成功!!!")
    # 打印回显示结果
    for name, val in varBinds:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))  # 打印修改的结果


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 设置主机名
    snmpv2_set("192.168.98.129", "tcpiprw", "1.3.6.1.2.1.1.5.0", "Net_R1", port=161)
    # shutdown G2
    snmpv2_set("192.168.98.129", "tcpiprw", "1.3.6.1.2.1.2.2.1.7.2", 2, port=161)