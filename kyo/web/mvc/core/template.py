#!/usr/bin/env python3

from request import Request
from response import Response
from config import Config
import os


class Template:

    def __init__(self, filename=None, **kwargs):
        self.filename = Config.ROOT + "/"

        default = [Request.app, Config.NAME['VIEW'],
                   Request.mod, Request.controller]
        l = 0
        if filename is not None:
            l = 4 if filename.startswith('/') else len(filename.split('/'))

        self.filename += '/'.join(default[:4 - l])
        self.filename += '/%s' % filename if filename else ''
        self.filename += ".%s" % Config.TEMPLATE_SUFFIX
        self.filename = os.path.realpath(self.filename)

        self.tempVar = {}
        self.tempVar.update(kwargs)


    def fetch(self, **kwargs):
        self.tempVar.update(kwargs)

        html = ""
        with open(self.filename) as f:
            html = f.read()

        return html.format(**self.tempVar)

    def show(self, **kwargs):
        return Response(self.fetch(**kwargs))


def render(filename=None, response=True, context={}):
    t = Template(filename, **context)
    return t.show() if response else t.fetch()
