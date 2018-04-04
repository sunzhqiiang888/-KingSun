#!/usr/bin/env python3

def isleap(year):
    """
    判断输入年是否为闰年
    """
    return 1 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 0


def yearDays(sy, ey):
    """
    计算两个年之间天数
    """
    days = 0
    while sy < ey:
        days += 365 + isleap(sy)
        sy += 1
    #  for i in range(sy, ey):
        #  days += 365 + isleap(i)
    return days


def monthDays(year, month):
    """
    计算输入月之前的天数
    """
    #  days = (month - 1) * 30 + month // 2
    #  days += 1 if month in (9, 11) else 0
    #  days -= 2 - isleap(year) if month > 2 else 0
    #  return days

    M = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
         (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))[isleap(year)]

    days = 0
    for i in range(month - 1):
        days += M[i]

    return days


def checkDate(year, month, day):
    """
    计算输入年月日是否合法
    年: 1900 - 2100
    """
    #  if (year < 1900 or year > 2100 or month < 1 or month > 12 or day < 1
        #  or (month in (4, 6, 9, 11) and day > 30)
        #  or (month == 2 and day > 28 + isleap(year))
        #  or day > 31):
        #  return False

    if year < 1900 or year > 2100 or month < 1 or month > 12 or day < 1:
        return False

    if month in (4, 6, 9, 11) and day > 30:
        return False

    if month == 2 and day > 28 + isleap(year):
        return False

    if day > 31:
        return False

    return True




