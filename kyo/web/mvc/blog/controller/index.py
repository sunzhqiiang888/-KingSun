#!/usr/bin/env python3


from response import Response
from template import Template, render
from config import Config
import MySQLdb


def index(request, *args):
    context = {}
    context['data_list'] = ''
    for i in range(10):
        context['data_list'] += render("panel", False)
    context['title'] = '~~~~~~~'
    context['site_name'] = "Python的博客"
    context['css'] = Config.CSS
    context['js'] = Config.JS
    return render(context=context)


def student(request, *args):
    context = {}
    context['data_list'] = ''

    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root',
                           passwd='123123', db='company', charset='utf8')

    #  cursor = conn.cursor()
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("select * from emp")
    result = cursor.fetchall()
    for row in result:
        context['data_list'] += '<tr>'
        context['data_list'] += '<td>%s</td>' % row['ename']
        context['data_list'] += '<td>%s</td>' % row['birthday']
        context['data_list'] += '<td>%s</td>' % row['sex']
        context['data_list'] += '</tr>'

    conn.commit()
    cursor.close()
    conn.close()

    context['option_list'] = ''

    return Template().show(**context)
