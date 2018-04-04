#!/usr/bin/env python3


import os
import sys
from udp import *
#  from threading import Thread
from select import select

class Chat:

    def write(self):
        #  print("write.....")
        data = input("发送: ")
        if not data:
            return

        self.send(data, ack_timeout=2)

        if data == 'exit' or data == 'q':
            return True


    def read(self):
        data = self.recv(PT_DATA, ack_type=PT_DATA_ACK).decode()

        if data == 'exit' or data == 'q':
            return True

        print("接受: %s" % (data))


    def do(self):
        #  Thread(target=self.read).start()
        try:
            inputfd = sys.stdin.fileno()
            netfd = self.sd.fileno()
            while True:
                r, *o = select([inputfd, netfd], [], [])
                #  print(r)
                if inputfd in r:
                    if self.write():
                        return print("发送退出请求...")

                if netfd in r:
                    if self.read():
                        return print("接受到对方发送退出请求...")
        except:
            pass


class ChatSrv(UdpSrv, Chat):

    def auth(self, data, addr):
        passwd = getattr(self, 'passwd', None)
        print(">>>>>>", data, passwd)
        if passwd is not None and data != passwd:
            raise Exception('密码验证失败!')

        if not hasattr(self, 'cli_addr'):
            self.cli_addr = addr
        elif self.cli_addr != addr:
            raise Exception('非法用户!')

        self.ip, self.port = addr


    def handle(self, data, addr, sd):
        try:
            self.auth(data.decode(), addr)
            self.sd = sd
            self.send("ok", addr, packet_type=PT_CONN_ACK)
        except Exception as e:
            self.send(str(e), addr, sd, packet_type=PT_ERROR)
            return

        self.do()


class ChatClient(UdpCli, Chat):

    def do(self, passwd):
        try:
            data = self.connect(passwd, 3).decode()
            if data != 'ok':
                return print(data)
        except Exception as e:
            return print("连接服务器超时...", e)

        Chat.do(self)

