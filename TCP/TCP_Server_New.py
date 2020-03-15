#!/usr/bin/env python3
# coding:gbk

import socket
import select

# import select
# select ��windows��ֻ�ܼ��socket
# ��Linux�¿��Լ������i/o
# stdin,stdout,stderr = select.select(rlist,wlist,xlist,[timeout])
# rlist ��ص�׼�����Ķ���
# wlist ��ص�׼��д�Ķ���
# xlist ��ش���

# stdin ������Ķ��������仯��ֵ
# stdout ���д�Ķ��������仯��ֵ
# stderr �����������ֵ
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ʵ����socket����
sock.setblocking(False)  # ����Ϊ������ʽsocket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ����˿ڱ�socketʹ�ù���
# ��������socket.close()���ر����ӣ�
# ����ʱ�˿ڻ�û���ͷţ�
# Ҫ����һ��TIME_WAIT�Ĺ���֮�����ʹ�ã�
# Ϊ��ʵ�ֶ˿ڵ����ϸ��ã�
# ����ѡ��setsockopt()�������ﵽĿ�ġ�
sock.bind(("", 8000))  # ����˰�ip,�˿�
sock.listen(5)  # �����˿�
inputs = [sock]  # ʵ����һ���б���sock�����б���
outputs = []  # ʵ����һ�����б�
errputs = []  # ʵ����һ�����б�

while True:
    # ���ü����Ķ��󣬲��ҷ�����������
    stdin, stdout, stderr = select.select(inputs, outputs, errputs, 1)
    # print(stdin, stdout, stderr)
    if stdin:  # �������ж�����Ҳ����׼��Ҫ���������б仯��������ֵ
        for s in stdin:  # ����ֵΪ�б�
            # Ԫ���п�����sock����
            print(stdin)  # ��ӡ
            if s is sock:  # �жϷ��ص���sock��������
                con, add = s.accept()  # ����ǣ���������
                print("%s:%s is connectd" % add)  # ��ӡ���������
                inputs.append(con)  # ��con����inputs

            else:  # �������sock������ s �������sock����con
                data = s.recv(512)  # ��������
                if not data:  # �������Ϊ��
                    inputs.remove(s)  # ���б���ɾ��s����
                else:
                    print(data)  # ��ӡ���յ�����
