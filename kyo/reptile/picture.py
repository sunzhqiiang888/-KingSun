#!/usr/bin/env python3

import requests
import os

url = "https://www.bilibili.com/video/av1349282/?p=1"
root = "/tmp/pic/"
path = root + url.split("/")[-1]

def picture(root,url,path):
    try:
        if not os.path.exists(root):#判断文件夹是否存在
            os.mkdir(root)
        if not os.path.exists(path):#判断文件是否存在
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)#r.content是爬取文件的二进制形式
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬去失败")



if __name__ == "__main__":
    def main():
        picture(root,url,path)

    main()
