#!/usr/bin/env python3


import socket


if __name__ == "__main__":
    def main():

        sd = socket.socket()
        sd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sd.bind(('0.0.0.0', 9000))
        sd.listen()

        while True:
            cli_sd, addr = sd.accept()
            print(addr, "连接上来...")

            while True:
                data = cli_sd.recv(1024)
                if data.decode().rstrip('\n') == 'q':
                    break
                cli_sd.send(data)

            cli_sd.close()

        sd.close()

    main()
