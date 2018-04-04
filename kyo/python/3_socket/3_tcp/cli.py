#!/usr/bin/env python3


import socket


if __name__ == "__main__":
    def main():

        sd = socket.socket()
        sd.connect(('192.168.7.170', 9000))

        while True:
            data = input("发送: ")

            sd.send(data.encode())

            if data == 'q':
                break

            print(sd.recv(1024).decode())

        sd.close()

    main()
