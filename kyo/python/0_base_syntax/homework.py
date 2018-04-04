#!/usr/bin/env python3

from mydate import *
from common import *

"""
实现cal功能
    time.time()     返回从1970年1月1号0点0分0秒到现在有多少秒(格林时区)

    (time.time() / 60 / 60 + 8) / 24

判断用户输入数是否回文数(111, 121, 12321)
判断用户输入数是否完数(所有因子之和等于它本身)
输出1-1/2+1/3-1/4+1/5...+1/99-1/100结果(保留两位小数点)
求1000以内的水仙花数(每位立方之和等于它本身)
把八进制数转化为十进制数输出
实现菜单打印图形
    1. 直角三角形(四种, 考虑一个循环实现)
    2. 梯形
    3. 正方形
    4. 退出

        按1输出子菜单:
            1). 右上
            2). 右下
            3). 左下
            4). 左上
            5). 返回上一级

输入5, 输出:
    * * * * *
      * * * *
        * * *
          * *
            *
"""

def ball():
    """
    一个袋子里有3个红球， 3个绿球，6个黄球， 一次从袋子里取6个球，列出所有可能的颜色组合
    """
    r = 0
    while r < 4:
        g = 0
        while g < 4:
            print("红球: %d, 绿球: %d, 黄球: %d" % (r, g, 6 - r - g))
            g += 1
        r += 1

def buy():
    """
    公鸡5元一只，母鸡3元一只，小鸡1元3只，现在打算用100元买一百只鸡，列出所有可能的组合
    """
    n = 100
    m = 100

    g1 = m // 5
    g2 = m // 3


    i = 0
    while i <= g1:
        j = 0
        while j <= g2:
            k = n - i - j
            if k % 3 == 0 and i * 5 + j * 3 + k // 3 == 100:
                print("公鸡: %d只, 母鸡: %d只, 小鸡: %d只" % (i, j, k))
            j += 1
        i += 1

def mul9x9():
    """
    9x9乘法(一个循环)
    """
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d x %d = %2d " % (i, j, i * j), end='')
            j += 1
        print()
        i += 1

def blackFriday():
    """
    已知1900年一月一号是星期一, 问今年有多少个黑色星期五(黑色星期五每个月13号是星期五)
    """
    def run(year):
        days = yearDays(1900, year) + 13

        for i in range(1, 13):
            if (days + monthDays(year, i)) % 7 == 5:
                print("%4d年%2d月13号是黑色星期五!" % (year, i))

    repeat(run, itype=int, prompt="请输入年份: ")

def fish():
    """
    某人从2000年一月一号开始过着3天打鱼两天晒网的日子，输入年月日判断此人在打鱼还是晒网
    """
    def do(year, month, day):
        if not checkDate(year, month, day):
            return print("日期不合法...")

        days = (yearDays(2000, year) + monthDays(year, month) + day) % 5
        if 1 <= days <= 3:
            print("打鱼")
        else:
            print("晒网")

    repeat(do, itype=int, prompt="请输入年月日: ", seq=' ')

def divisor():
    """
    求两个数最大公约数
    """
    def do(n1, n2):
        for i in range(n2 if n1 > n2 else n1, 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                return print("%d 和 %d的最大公约数是: %d" % (n1, n2, i))

    repeat(do, itype=int, prompt="请输入两个整数: ", seq=' ')

def fourNum():
    """
    4, 5, 6, 7能组合多少个不能被4整除的4位数(位数不能相同，考虑一个循环实现)
    """
    n = 4 + 5 + 6 + 7
    count = 0
    for i in range(4, 8):
        for j in range(4, 8):
            if i == j:
                continue
            for k in range(4, 8):
                if i == k or j == k:
                    continue
                l = n - i - j - k

                s = i * 1000 + j * 100 + k * 10 + l
                if s % 4 != 0:
                    count += 1
                    print("%d " % s, end="")

    print("\ncount = %d" % count)

    count = 0
    for n in range(4567, 7655):
        i = n // 1000 % 10
        j = n // 100 % 10
        k = n // 10 % 10
        l = n // 1 % 10

        if (4 <= i <= 7 and 4 <= j <= 7
            and 4 <= k <= 7 and 4 <= l <= 7
            and i != j and i != k and i != l
            and j != k and j != l and k != l
            and n % 4 != 0):
            count += 1
            print("%d " % n, end="")

    print("\ncount = %d" % count)


def main():
    cmd = (ball, buy, mul9x9, blackFriday, fish, divisor, fourNum)
    menulist = ["拿球", "买鸡", "乘法表", "黑色星期五", "打鱼晒网", "公约数",
                "组合4位数"]
    #  menulist = open("./menu.list").readlines()

    menu(menulist, cmd)

main()


