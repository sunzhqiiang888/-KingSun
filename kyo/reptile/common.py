#!/usr/bin/env python3
import requests
import sys

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
 #       c = r.status_code
        #  print(c)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        #  print(r.request.headers)
        return r.text
    except:
        return "出现错误"

if __name__ == "__main__":
    def main():
        url = sys.argv[1]
        print(getHTMLText(url),end="")

    main()
