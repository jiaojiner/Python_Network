#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
# 该代码由本人学习时编写，仅供自娱自乐！
# 本人QQ：1945962391 
# 欢迎留言讨论，共同学习进步！

import dns.resolver


def dnspython(domain, Type="A"):
    result = dns.resolver.query(domain, Type)
    # print(result)
    return_result = []
    if Type == "A" or Type == "AAAA":
        for i in result.response.answer:
            # print(i)
            for j in i:
                # print(type(j))
                return_result.append(j.address)
    elif Type == "CNAME" or Type == "NS":
        for i in result.response.answer:
            for j in i:
                return_result.append(j.to_text())
    elif Type == 'MX':
        for i in result:
            return_result.append({'MX preference': i.preference, 'mail exchanger': i.exchange.to_text()})
    return return_result


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    print(dnspython("cisco.com", Type="A"))
    print(dnspython("cisco.com", Type="AAAA"))
    print(dnspython("www.cisco.com", Type="CNAME"))
    print(dnspython("cisco.com", Type="NS"))
    print(dnspython("cisco.com", Type="MX"))
