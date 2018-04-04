#!/usr/bin/env python3

from random import choice
from base import Base
from randata import randData

class Classes(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)
        self.table = 'class'
        self.md5Field = ['name', 'sid', 'state']
        self.sid = self.getSid()
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, **kwargs):
        data['sid'] = self.randSid(sid)
        sql = """select c.name as name, l.addtime as addtime
                 from lecture l join course c on c.id=l.cid
                 where l.sid=%s""" % data['sid']
        course = self.db.query(sql)
        if len(course) <= 0:
            return None
        c = choice(course)
        data['name'] = c['name'] + choice(self.cnNum) + "班"
        data.update(self.getTime(date, c['addtime']))
        return data

if __name__ == '__main__':
    s = Classes(5, 0, '3y')
    s.rand(sid=2)
