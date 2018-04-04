#!/usr/bin/env python3
import sys
import requests

url = "http://m.ip138.com/ip.asp?ip="

def ipaddr(url,ip):
    url = url + ip
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-1000:])
    except:
        print("爬取ip信息失败")




if __name__ == "__main__":
    def main():
        ip = sys.argv[1]
        ipaddr(url,ip)

    main()
