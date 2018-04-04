#!/usr/bin/env python3

from random import choice
from base import Base
from randata import randData

class Lecture(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)
        self.table = 'lecture'
        self.md5Field = ['sid', 'tid', 'cid']
        self.sid = self.getIdList('school')
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, **kwargs):
        data = {}
        data['sid'] = self.randSid(sid)
        data['tid'] = choice(self.getIdList('teacher', 'sid=%s' % data['sid']))
        data['cid'] = choice(self.getIdList('course', 'sid=%s' % data['sid']))

        t_time = self.getAddTime('teacher', data['tid'])
        c_time = self.getAddTime('course', data['cid'])

        data.update(self.getTime(date, t_time if t_time > c_time else c_time))

        return data

if __name__ == '__main__':
    s = Lecture(5, 0, '3y')
    s.rand()
