#!/usr/bin/env python3

from school import School
from teacher import Teacher
from course import Course
from classes import Classes
from lecture import Lecture
from dispatch import Dispatch
from student import Student
from choose import Choose
from score import Score
import sys
from base import Base
from getopt import getopt

class Clear(Base):

    def rand(self, *args, **kwargs):
        sql = "truncate table school;"
        sql += "truncate table teacher;"
        sql += "truncate table class;"
        sql += "truncate table course;"
        sql += "truncate table lecture;"
        sql += "truncate table dispatch;"
        sql += "truncate table student;"
        sql += "truncate table score;"
        sql += "truncate table choose;"
        self.db.execute(sql)


if __name__ == "__main__":
    def main():
        assert len(sys.argv) > 1, "参数个数指定有误!"

        Cmd = {
            'school': School,
            'teacher': Teacher,
            't': Teacher,
            'course': Course,
            'c': Course,
            'classes': Classes,
            'class': Classes,
            'lecture': Lecture,
            'l': Lecture,
            'dispatch': Dispatch,
            'd': Dispatch,
            'student': Student,
            's': Student,
            'choose': Choose,
            'score': Score,
            'clear': Clear
        }

        Cls = Cmd.get(sys.argv[1], None)
        assert Cls is not None, "不支持传入的命令!"

        opt, args = getopt(sys.argv[2:], "n:s:d:", ['sid=', 'cid='])
        opt = dict(opt)

        num = int(opt.get('-n', 10))
        state = int(opt.get('-s', 0))
        date_str = opt.get('-d', '3y')
        sid = opt.get('--sid', None)
        sid = int(sid) if sid is not None else sid
        cid = opt.get('--cid', None)
        cid = int(cid) if cid is not None else cid

        o = Cls(num, state, date_str)
        o.rand(sid=sid, cid=cid)

        #  s = School(3, 0, '3y')
        #  s.rand()

        #  t = Teacher(10, 0, '3y')
        #  t.rand(sid=1)
        #  t.rand(sid=2)
        #  t.rand(sid=3)

        #  c = Course(10, 0, '3y')
        #  c.rand(sid=1)
        #  c.rand(sid=2)
        #  c.rand(sid=3)

        #  l = Lecture(5, 0, '3y')
        #  l.rand(sid=1)
        #  l.rand(sid=2)
        #  l.rand(sid=3)

        #  e = Classes(3, 0, '3y')
        #  e.rand(sid=1)
        #  e.rand(sid=2)
        #  e.rand(sid=3)

        #  e = Dispatch(3, 0, '3y')
        #  e.rand(sid=1)
        #  e.rand(sid=2)
        #  e.rand(sid=3)

        #  e = Student(20, 0, '3y')
        #  e.rand(sid=1)
        #  e.rand(sid=2)
        #  e.rand(sid=3)

        #  e = Choose(10, 0, '3y')
        #  e.rand(sid=1)
        #  e.rand(sid=2)
        #  e.rand(sid=3)

        #  e = Score(10, 0, '3y')
        #  e.rand(sid=1)
        #  e.rand(sid=2)
        #  e.rand(sid=3)

    main()
