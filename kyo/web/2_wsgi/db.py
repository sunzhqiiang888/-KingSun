#!/usr/bin/env python3


import MySQLdb


def index():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root',
                           passwd='123123', db='company', charset='utf8')

    #  cursor = conn.cursor()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("select * from emp")
    result = cursor.fetchall()
    for row in result:
        print(row['ename'])

    conn.commit()
    cursor.close()
    conn.close()
    return ""

index()

