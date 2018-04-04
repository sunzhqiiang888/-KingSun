#!/usr/bin/env python3
import sys

import requests

from bs4 import BeautifulSoup

import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:#遍历tbody的子标签tr
        if isinstance(tr, bs4.element.Tag):#判断tr的类型是否是bs4库定义的tag类型
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校", "省份", chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


if __name__ == "__main__":
    def main():
        uinfo = []
        url = sys.argv[1]
        html = getHTMLText(url)
        fillUnivList(uinfo, html)
        printUnivList(uinfo, 20)

    main()
