#!/usr/bin/env python3


from urllib.parse import parse_qs


class Request:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if Request.__instance is None:
            Request.__instance = object.__new__(cls)
        return Request.__instance

    def __init__(self, env):
        env['PATH_INFO'] = env['PATH_INFO'].encode('iso-8859-1').decode('utf-8')
        env['QUERY_STRING'] = env['QUERY_STRING'].encode('iso-8859-1').decode('utf-8')
        self.env = env
        self.method = env['REQUEST_METHOD']
        self.type = env['CONTENT_TYPE']
        self.length = env['CONTENT_LENGTH']
        self.path = env['PATH_INFO']

        self.host = env['HTTP_HOST']
        self.addr = env['REMOTE_ADDR']
        self.agent = env['HTTP_USER_AGENT']
        self.accept = env['HTTP_ACCEPT']
        self.accept_language = env['HTTP_ACCEPT_LANGUAGE']
        self.accept_encoding = env['HTTP_ACCEPT_ENCODING']

        self.IS_GET = bool(self.method == 'GET')
        self.IS_POST = bool(self.method == 'POST')
        self.IS_PUT = bool(self.method == 'PUT')
        self.IS_DELETE = bool(self.method == 'DELETE')

        self.get = self.parse(env['QUERY_STRING'])

        self.url = env['wsgi.url_scheme'] + "://" + self.host + self.path

        for k, v in self.__dict__.items():
            setattr(Request, k, v)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        setattr(Request, name, value)

    def parse(self, qs):
        data = {}

        for k, v in parse_qs(qs).items():
            data[k] = v if len(v) > 1 else v[0]

        return data


    @staticmethod
    def items():
        return Request.__instance.__dict__.items()

#  wsgi.input: <_io.BufferedReader name=4>
#  wsgi.errors: <_io.TextIOWrapper name='' mode='w' encoding='UTF-8'>






