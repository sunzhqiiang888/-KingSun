#!/usr/bin/env python3

from random import choice
from base import Base
from randata import randData

class School(Base, randData):

    def __init__(self, num, state=None, range_time=None, **kwargs):

        Base.__init__(self, num, state, range_time)

        self.table = 'school'
        self.md5Field = ['name', 'location', 'state']
        self.city = self.getCity()
        self.__dict__.update(kwargs)

    def errCount(self):
        total = self.db.col("select count(*) as total from %s" % self.table)
        return len(self.city) * len(self.cnNum) * len(self.sub) - total


    def field(self, data, date, **kwargs):
        city = choice(self.city)
        data['name'] = city + '第' + choice(self.cnNum) + choice(self.sub)
        data['location'] = "%s市" % city
        data.update(self.getTime(date))
        return data


if __name__ == '__main__':
    s = School(10, 0, range_time='3y')
    s.rand()


