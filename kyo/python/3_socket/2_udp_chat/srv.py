#!/usr/bin/env python3


import sys
from chat import ChatSrv


if __name__ == "__main__":
    def main():
        passwd = sys.argv[1] if len(sys.argv) > 1 else "123"

        srv = ChatSrv(passwd=passwd)
        try:
            srv.run()
        except:
            ...  #pass

    main()
