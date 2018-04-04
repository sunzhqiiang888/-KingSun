#!/usr/bin/env python3
import os

def my_ls(path):
    print(path)
    l = os.listdir(path)
    print(l)
    for filename in l:
        filename = path + '/' + filename
        if os.path.isdir(filename):
            my_ls(filename)
            print("目录：", filename)
        else:
            print("文件:", filename)
if __name__ == "__main__":
    def main():
        my_ls(input("请输入一个路径："))

    main()
