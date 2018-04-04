#!/usr/bin/env python3


import sys
from chat import ChatClient


if __name__ == "__main__":
    def main():
        ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.7.170"
        passwd = sys.argv[2] if len(sys.argv) > 2 else "123"
        port = sys.argv[3] if len(sys.argv) > 3 else 9000

        cli = ChatClient(ip=ip, port=port)
        cli.do(passwd)


    main()
