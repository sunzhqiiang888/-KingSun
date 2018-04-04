#!/usr/bin/env python3


from http import HTTPStatus
from request import Request


class Response:

    def __init__(self, body, status=200, content_type=None,
                 header={}, **kwargs):
        self.body = body if isinstance(body, bytes) else body.encode()

        self.status = "%d %s" % (status, HTTPStatus(status).name)

        if content_type is None:
            content_type = 'text/html; charset=utf-8'

        self.header = {'Content-Type': content_type}
        self.header.update(header)
        self.header = list(self.header.items())

        self.__dict__.update(kwargs)


class StaticResponse(Response):

    def __init__(self, path, **kwargs):
        body = None

        with open(path, "rb") as f:
            body = f.read()

        Response.__init__(self, body, content_type=Request.accept, **kwargs)

