#!/usr/bin/env python3

from datetime import datetime
from random import randint
from dateutil.relativedelta import relativedelta
#  relativedelta由第三方库提供, 第三方的日期处理库: python-dateutil
    #  pip3 install python-dateutil

class Date:

    """
    随机日期时间:
        时间戳: 从1970年1月1号0点0分0秒到现在有多少秒(格林)
    """

    CMD = {'y': 'years', 'm': 'months', 'd': 'days',
           'H': 'hours', 'M': 'minutes', 'S': 'seconds', 'w': 'weeks'}

    def __init__(self, range_str=None):
        if range_str is None:
            self.start = self.end = datetime.now()
        else:
            self.start, self.end = self.parse(range_str)

    def rand_dt(self, start=None, end=None):
        start = start or self.start
        end = end or self.end
        m = randint(int(start.timestamp()), int(end.timestamp()))
        return datetime.fromtimestamp(m)

    def rand(self, start=None, end=None, format="%F %T"):
        return self.rand_dt(start, end).strftime(format)

    @staticmethod
    def parse(range_str):
        """
        解析字符串生成起始日期和结束日期
            2y      2年内(从2年前到现在的范围)
            -2y     2年内(从2年前到现在的范围)
            2m      2个月内
            2d      2天内
            2H      2时内
            2M      2分钟内
            2S      2秒内
            2w      2周内
            +2y     2年内(从现在到2年后的范围)

            -5:-3y  5年前到3年前的范围
            -5:3y   5年前到3年后的范围
            3:5y    3年后到5年后的范围
        """

        range_str = range_str.strip()

        name = Date.CMD.get(range_str[-1], None)
        if name is None:
            raise Exception("范围字符命令格式错误")

        range_str = range_str[:-1]

        now = datetime.now()

        if ':' in range_str:
            s, e = range_str.split(':')
            return (now + relativedelta(**{name: int(s)}),
                    now + relativedelta(**{name: int(e)}))

        range_str = range_str if range_str[0] in '+-' else '-' + range_str
        newTime = now + relativedelta(**{name: int(range_str)})

        if now > newTime:
            return newTime, now
        return now, newTime

