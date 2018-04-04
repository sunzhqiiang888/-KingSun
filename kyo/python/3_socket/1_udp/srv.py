#!/usr/bin/env python3


import socket


if __name__ == "__main__":
    def main():
        #  创建操作系统提供UDP传输协议的编程接口, 返回UDP套接字对象
        sd = socket.socket(type=socket.SOCK_DGRAM)

        #  给套接字对象绑定IP和端口号(必须1024以上, 65535以内)
        sd.bind(('0.0.0.0', 9000))

        while True:
            #  等待客户端请求
            data, addr = sd.recvfrom(1024)

            #  处理客户端请求
            print("%s: %s" % (addr, data.decode()))

        #  关闭套接字对象
        sd.close()

    main()
