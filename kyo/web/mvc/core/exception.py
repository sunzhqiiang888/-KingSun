#!/usr/bin/env python3


from response import Response
from request import Request
from config import Config
from datetime import datetime
import sys
import traceback


class MVCException:

    httpState = {
        'ImportError': 404,
    }

    @staticmethod
    def debug(name, msg, tb):
        errfile = '<span style="color:green">%s</span>'
        errfile = errfile % tb[-1].split('\n')[0].strip()
        s = "<h2>"
        s += '请求信息:&emsp;<span style="color:blue">%s</span><br><br>'
        s += "异常信息&nbsp;(%s):<br><br>"
        s += '&emsp;&emsp;<span style="color:blue">%s</span><br><br>'
        s = s % (Request.url, errfile, msg)

        s += "异常类:<br>&emsp;&emsp;%s</br><br>" % name.__name__

        s += "异常栈信息: <br>"
        for i in tb:
            m = i.split("\n")
            s += "&emsp;&emsp;" + m[0] + "<br>"
            s += '&emsp;&emsp;&emsp;&emsp;<span style="color:red">'
            s += m[1]
            s += '</span><br><br>'

        s += "<hr>"
        s += "配置信息: <br><br>"
        for k, v in Config.items():
            if not isinstance(v, dict):
                s += '%s: <span style="color: #666">%s</span><br><br>' % (k, v)
                continue

            s += '%s: <br><br>' % k

            for ks in v:
                s += '&emsp;&emsp;'
                s += '%s: <span style="color: #666">%s</span><br><br>'
                s = s % (ks, v[ks])

        s += "<hr>"
        s += "环境变量: <br><br>"
        for e in Request.env:
            s += '%s: <span style="color: #666">%s</span>' % (e, Request.env[e])
            s += '<br><br>'

        s += "</h2>"

        return s

    @staticmethod
    def log(name, msg, tb):
        #  时间 IP PATH 错误位置 错误信息
        time = datetime.now().strftime("%F %T")
        errfile = tb[-1].split('\n')[0].strip()
        s = "[%s] %s->%s (%s) %s" % (time, Request.addr, Request.path,
                                     errfile, msg)

        print(s, file=open(Config.LOG_FILE, "a"))

        return '<h1>%s</h1>' % Config.DEFAULT['ERROR']

    @staticmethod
    def do():
        name, msg, tb = sys.exc_info()
        tb = traceback.format_tb(tb)

        if Config.DEBUG:
            body = MVCException.debug(name, msg, tb)
        else:
            body = MVCException.log(name, msg, tb)

        return Response(body, MVCException.httpState.get(name.__name__, 400))


