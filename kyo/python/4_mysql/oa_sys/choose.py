#!/usr/bin/env python3

from random import choice
from base import Base
from randata import randData

class Choose(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)
        self.table = 'choose'
        self.md5Field = ['cid', 'sid']
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, **kwargs):
        sigCon = '1' if sid is None else "sid=%s" % sid
        sql = "select id, cid, sid, addtime from student where %s" % sigCon
        s = choice(self.db.query(sql))

        data['sid'] = s['id']
        data['cid'] = choice(self.getIdList('course', 'sid=%s' % s['sid']))

        data.update(self.getTime(date, s['addtime']))

        return data

if __name__ == '__main__':
    s = Choose(5, 0, '3y')
    s.rand(sid=1)
