#!/usr/bin/env python3


class MVC:
    def __call__(self, env, start_response):
        path = env['PATH_INFO'].split('/')
        pathCount = len(path)
        filename = path[1] or 'index'
        method = path[2] if pathCount > 2 else 'index'
        args = path[3:] if pathCount > 3 else []

        try:
            m = __import__(filename)
            body = getattr(m, method)(*args)
            if not isinstance(body, (str, bytes)):
                raise Exception("返回值类型不对...")
        except Exception as e:
            body = str(e)

        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

        return [body.encode() if isinstance(body, str) else body]


