#!/usr/bin/env python3

from random import choice, randint
from base import Base
from randata import randData

class Score(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)
        self.table = 'score'
        self.md5Field = ['cid', 'score']
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, start=0, end=100, **kwargs):
        sigCon = '1' if sid is None else "sid=%s" % sid
        sql = "select id, addtime from choose where %s" % sigCon
        c = choice(self.db.query(sql))

        data['cid'] = c['id']
        score = randint(start, end)
        if score != 100:
            score += randint(0, 1) * 0.5
        data['score'] = score

        data.update(self.getTime(date, c['addtime'], update=False))

        return data

if __name__ == '__main__':
    s = Score(5, 0, '3y')
    s.rand(sid=1, start=60)
