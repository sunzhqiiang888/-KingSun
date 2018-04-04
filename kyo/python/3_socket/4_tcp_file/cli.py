#!/usr/bin/env python3


import socket
import sys


if __name__ == "__main__":
    def main():
        filepath = sys.argv[1] if len(sys.argv) > 1 else "/tmp/1.txt"

        sd = socket.socket()
        sd.connect(('192.168.7.170', 9000))

        sd.send(filepath.encode())
        data = sd.recv(1024).decode()
        if data != 'ok':
            return print(data)

        fp = open(r"./down.file", "wb")

        while True:
            data = sd.recv(1024)

            fp.write(data)

            sd.send("ack".encode())

            if len(data) < 1024:
                break

        fp.close()
        sd.close()

    main()
