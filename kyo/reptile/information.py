#!/usr/bin/env python3

import sys

import re

from bs4 import BeautifulSoup

import requests

def getUrl(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现错误"


def beauti(demo):
    soup = BeautifulSoup(demo, "html.parser")
    #  for link in soup.find_all('a'):
        #  print("http:%s"%link.get('href'))
    for link in soup.find_all(name="d")
        print(link)


if __name__ == "__main__":
    def main():
        url = sys.argv[1]
        beauti(getUrl(url))

    main()
