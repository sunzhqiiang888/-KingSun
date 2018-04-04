#!/usr/bin/env python3


import socket
import http.client
import urllib.request


if __name__ == "__main__":
    def main():
        sd = socket.socket()
        sd.connect(('47.52.106.36', 80))

        sd.send("GET /\r\nContent-Type: text/html; charset=utf-8\r\n".encode())
        while True:
            data = sd.recv(1024)
            if not data:
                break
            print(data.decode(), end='')

        sd.close()

    def httpClient():
        conn = http.client.HTTPConnection("jaja.cc")
        conn.request("GET", "/")
        r = conn.getresponse()
        print(r.status, r.reason)
        print(r.read())
        r.close()

    def urllibTest():
        f = urllib.request.urlopen("http://jaja.cc")
        print(f.read())


    #  main()
    #  httpClient()
    urllibTest()
