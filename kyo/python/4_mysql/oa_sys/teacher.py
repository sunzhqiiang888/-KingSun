#!/usr/bin/env python3

from random import randint, choice
from base import Base
from randata import randData

class Teacher(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)

        self.table = 'teacher'
        self.md5Field = ['name', 'sid', 'state', 'gender']
        self.sid = self.getSid()
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, **kwargs):
        data['name'] = self.getName
        data['sid'] = self.randSid(sid)
        data['gender'] = randint(0, 1)

        data.update(self.getTime(date, self.getAddTime('school', data['sid'])))

        return data

if __name__ == '__main__':
    s = Teacher(5, 0, '3y')
    s.rand(sid=1)
