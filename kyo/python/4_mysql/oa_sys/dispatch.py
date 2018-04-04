#!/usr/bin/env python3

from random import choice
from base import Base
from randata import randData

class Dispatch(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):
        Base.__init__(self, num, state, range_time)
        self.table = 'dispatch'
        self.md5Field = ['sid', 'tid', 'cid']
        self.__dict__.update(kwargs)

    def field(self, data, date, sid=None, **kwargs):
        data = {}
        try:
            sidCon = "1" if sid is None else "sid=%s" % sid
            sql = "select id, sid, name from class where %s" % sidCon
            c = choice(self.db.query(sql))

            sql = """select l.id as id, l.addtime as addtime ,c.name as name
                     from lecture l join course c on c.id=l.cid
                     where l.sid=%s and '%s' like concat(c.name, '%%')
                  """ % (c['sid'], c['name'])
            l = choice(self.db.query(sql))

            data['sid'] = c['sid']
            data['cid'] = c['id']
            data['tid'] = l['id']

            data.update(self.getTime(date, l['addtime']))

            return data
        except Exception as e:
            #  print(e)
            return None

if __name__ == '__main__':
    s = Dispatch(5, 0, '3y')
    s.rand(sid=2)
