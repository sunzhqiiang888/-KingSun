#!/usr/bin/env python3

from random import choice
from base import Base
from randata import randData

class Course(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)
        self.table = 'course'
        self.sid = self.getSid()
        self.md5Field = ['name', 'sid', 'state']
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, **kwargs):
        data['name'] = choice(self.course)
        data['sid'] = self.randSid(sid)
        data.update(self.getTime(date, self.getAddTime('school', data['sid'])))
        return data

if __name__ == '__main__':
    s = Course(5, 0, '3y')
    s.rand(sid=2)
