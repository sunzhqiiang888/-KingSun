#!/usr/bin/env python3


import MySQLdb


class Db:

    def __init__(self, db, user='root', passwd='123123', host='127.0.0.1',
                 port=3306, charset='utf8', **kwargs):

        self.conn = MySQLdb.connect(user=user, passwd=passwd, host=host, db=db,
                                    port=port, charset=charset)
        if 'cursorArgs' in kwargs:
            self.cursorArgs = kwargs['cursorArgs']
        else:
            self.cursorArgs = MySQLdb.cursors.DictCursor

        self.cursor = self.conn.cursor(self.cursorArgs)

        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]

        if hasattr(self.cursor, name):
            return getattr(self.cursor, name)

        return getattr(self.conn, name)

    def use(self, dbname):
        self.execute('USE %s' % dbname)
        return self

    def query(self, sql):
        self.execute(sql)
        return self.fetchall()

    def row(self, sql):
        return self.query(sql)[0]

    def col(self, sql):
        return list(self.row(sql).values())[0]

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, name, msg, tb):
        self.close()


if __name__ == '__main__':
    #  db = Db('company')

    #  print(db.row("select * from emp limit 1"))
    #  print("-----------------------------------")
    #  print(db.col("select count(*) from emp"))
    #  print("-----------------------------------")

    #  for row in db.query("select * from emp"):
        #  print(row)

    #  db.close()


    with Db('company') as db:
        for row in db.query("select * from emp"):
            print(row)


