#!/usr/bin/env python3

from random import randint, choice
from base import Base
from randata import randData

class Student(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)

        self.table = 'student'
        self.md5Field = ['state', 'sid', 'cid', 'name', 'gender', 'phone']
        self.sid = self.getSid()
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, cid=None, **kwargs):
        sidCon = "1" if sid is None else 'sid=%s' % sid
        cidCon = "1" if cid is None else 'id=%s' % cid
        sql = """select id, sid, addtime
                 from class where %s and %s""" % (sidCon, cidCon)
        c = None
        try:
            c = choice(self.db.query(sql))
        except:
            return None

        data['name'] = self.getName
        data['sid'] = c['sid']
        data['cid'] = c['id']
        data['gender'] = randint(0, 1)
        data['phone'] = '1%s%s' % (choice('3578'), randint(100000000, 999999999))

        data.update(self.getTime(date, c['addtime']))

        return data

if __name__ == '__main__':
    s = Student(5, 0, '3y')
    s.rand(cid=1)
