#!/usr/bin/env python3
import requests
import sys

keyword = sys.argv[1]
def guanji(url):
    try:
        kv = {'wd':keyword}   #百度关键字查询key是wd    搜狗关键字查询是q
        r = requests.get(url,params=kv)
        #  b = r.status_code
        print(r.request.url)
        r.raise_for_status()
        print(len(r.text))
    except:
        print("爬出失败")

if __name__ == "__main__":
    def main():
        guanji(sys.argv[2])

    main()
