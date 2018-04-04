#!/usr/bin/env python3

from db import Db
import hashlib
from random import choice
from date import Date

class Base:

    db = None

    def __init__(self, num, state=None, range_time=None, **kwargs):
        """
            state的取值:
                0       正常
                1       草稿
                2       审核
                3       锁定
                4       删除
        """

        if Base.db is None:
            Base.db = Db('oa')

        self.__dict__.update(kwargs)
        self.num = num
        self.state = [0, 1, 2, 3, 4] if state is None else [state]
        self.date = Date(range_time)

    def getList(self, sql):
        """
        将查询结果转成列表
        """
        return [x.popitem()[1] for x in self.db.query(sql)]

    def add(self, data):
        """
        将数据添加到数据表中
        """
        keys = ""
        values = ""
        for k, v in data.items():
            keys += '%s,' % k
            values += "'%s'," % v

        keys = keys.rstrip(',')
        values = values.rstrip(',')

        sql = 'INSERT %s (%s) values (%s)' % (self.table, keys, values)
        #  print(sql)
        self.db.execute(sql)
        self.db.commit()

    def md5(self, data):
        """
        获取数据的md5检验和
        """
        md5Field = getattr(self, 'md5Field', list(data.keys()))
        m = "".join([str(data[x]) for x in md5Field])
        return hashlib.md5(m.encode()).hexdigest()

    def checkMd5(self, data):
        """
        判断数据检验和是否在数据库当中存在
        不存在返回数据检验和, 存在返回None
        """
        md5sum = self.md5(data)
        sql = "select md5sum from %s where md5sum='%s'" % (self.table, md5sum)
        try:
            self.db.col(sql)
        except:
            return md5sum

    def parse(self, num, state, range_time):
        """
        不修改类数据只供临时随机数据的参数解析
        """
        num = num or self.num
        if state is None:
            state = self.state
        else:
            state = state if isinstance(state, (list, tuple)) else [state]

        date = self.date if range_time is None else Date(range_time)

        return num, state, date

    def errCount(self):
        """
        默认的随机连续重复最多的次数
        """
        return 1000

    def rand(self, num=None, state=None, range_time=None, **kwargs):
        """
        随机数据的框架函数
        """
        num, state, date = self.parse(num, state, range_time)

        total = self.errCount()

        i = 0
        err = 0
        while i < num:
            data = self.getData(state, date, **kwargs)
            if not data:
                err += 1
                if err >= total:
                    break
                continue
            self.add(data)

            err = 0
            i += 1

    def getTime(self, date, start=None, end=None, update=True):
        """
        基类提供的随机添加和更新的接口
        以供子类组合随机数据使用
        """
        data = {}
        addtime = date.rand_dt(start, end)
        data['addtime'] = addtime.strftime("%F %T")
        if update:
            data['update_time'] = date.rand(addtime)
        return data

    def getData(self, state, date, **kwargs):
        """
        准备添加数据表的随机数据的组合
        """
        data = {}
        data['state'] = choice(state)

        data = self.field(data, date, **kwargs)
        if not data:
            return None

        md5sum = self.checkMd5(data)
        if not md5sum:
            return None
        data['md5sum'] = md5sum

        return data

    def close(self):
        """
        手工关闭数据库连接
        """
        self.db.close()

