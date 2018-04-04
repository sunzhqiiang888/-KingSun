#!/usr/bin/env python3


import socket
import os
import time


def client_handler(sd, addr):
    path = sd.recv(1024).decode()
    fp = None
    try:
        fp = open(path, "rb")
        sd.send('ok'.encode())
    except:
        return sd.send('文件无法操作...'.encode())

    time.sleep(1)

    while True:
        data = fp.read(1024)
        if not data:
            break
        sd.send(data)

        sd.recv(1024)

    fp.close()


if __name__ == "__main__":
    def main():

        sd = socket.socket()
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sd.bind(('0.0.0.0', 9000))
        sd.listen()

        while True:
            cli_sd, addr = sd.accept()
            print(addr, "连接上来...")

            client_handler(cli_sd, addr)

            cli_sd.close()

        sd.close()

    main()
