#!/usr/bin/env python3


import socket


if __name__ == "__main__":
    def main():
        #  创建操作系统提供UDP传输协议的编程接口, 返回UDP套接字对象
        sd = socket.socket(type=socket.SOCK_DGRAM)

        while True:
            data = input("请输入发送数据: ")
            if data == 'q':
                break
            sd.sendto(data.encode(), ('192.168.7.170', 9000))

        sd.close()

    main()
