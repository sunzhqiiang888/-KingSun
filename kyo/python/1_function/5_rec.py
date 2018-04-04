#!/usr/bin/env python3

import os
import common

#  10
    #  十进制: 10
    #  二进制: 1010
    #  八进制: 0o12
    #  十六进制: 0xa

#  100 / 8     4
#  12 / 8      4
#  1 / 8       1
        #  0

#  def toOct(num):
    #  n = 0
   #  s = 0
    #  while num:
        #  s += num % 8 * (10 ** n)
        #  num //= 8
        #  n += 1

    #  return '0o%d' % s

def toOct(num):
    return 0 if num == 0 else toOct(num // 8) * 10 + num % 8

#  100     14 * 10 + 4 144
#  12      1 * 10 + 4  14
#  1       0 * 10 + 1  1
#  0       0


def C():
    print("C start....")
    r = 10
    print("C end....")
    return r

def B():
    print("B start....")
    r = C()
    print("B end....")
    return r

def A():
    print("A start....")
    r = B()
    print("A end....")
    return r


def test(num):
    if num == 0:
        return
    print("test start: ", num)
    test(num - 1)
    print("test end: ", num)


def ls(path):
    print("%s: " % path)
    l = os.listdir(path)
    for filename in l:
        filepath = path + '/' + filename
        if os.path.isdir(filepath):
            print("\t目录: ", filename)
        else:
            print("\t文件: ", filename)
    print()

    for filename in l:
        filepath = path + '/' + filename
        if os.path.isdir(filepath):
            ls(filepath)


if __name__ == "__main__":
    def testOct():
        #  while True:
            #  r = input("请输入一个十进制整型: ")
            #  if r == 'q':
                #  break
            #  print(toOct(int(r)))
        #  def toOctTest(s):
            #  print(toOct(int(s)))
        #  common.repeat(toOctTest)
        common.repeat(lambda s: print(toOct(int(s))))

        #  test(999)
        #  print(A())

    def testList():
        ls(input("请输入列表的目录路径: "))

    #  testList()
    testOct()

