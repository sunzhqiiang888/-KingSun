#!/usr/bin/env python3

import sys

import requests

from bs4 import BeautifulSoup


def getUrl(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现错误"


def beauti(demo):
    soup = BeautifulSoup(demo, "html.parser")
    #  soup.a.name  #便签a的name
    #  tag = soup.a
    #  print(tag.attrs['class'],tag.attrs['href'])
    #  print(soup.a.string)
    #  p = soup.p
    #  print(p.string)
    #  print(soup.head)
    #  print(soup.head.contents)
    #  print(soup.body.contents,len(soup.body.contents))
    #  for child in soup.body.children:
        #  print(child)
    #  for child in soup.body.descendants:
        #  print(child)
    #  print(soup.title.parent)
#      for parent in soup.a.parents:
        #  if parent is None:
            #  print(parent)
        #  else:
            #  print(parent.name)
    for link in soup.find_all('a'):
        print(link.get('href'))


def do(func,url):
    func(url)


if __name__ == "__main__":
    def main():
        url = sys.argv[1]
        #beauti(getUrl(url))
        do(beauti,getUrl(url))


    main()
