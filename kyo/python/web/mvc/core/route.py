#!/usr/bin/env python3


from common import imp
from response import StaticResponse


class Route:

    def __init__(self, request, config):
        self.config = config
        self.request = request

        path = request.path.split('/')
        pathCount = len(path)

        request.app = path[1] or config.DEFAULT['APP']

        if pathCount > 2:
            request.mod = path[2]
        else:
            request.mod = config.DEFAULT['CONTROLLER']

        if pathCount > 3:
            request.controller = path[3]
        else:
            request.controller = config.DEFAULT['METHOD']

        request.args = path[4:] if pathCount > 4 else []

        self.package = request.app + '.' + self.config.NAME['CONTROLLER']

        config.loadApp(request.app)

    def isStaticRequest(self):
        r = self.request
        c = self.config
        if c.NAME['STATIC'] in (r.app, r.mod, r.controller):
            return True
        return False

    def dispatch(self):
        if self.isStaticRequest():
            return StaticResponse(self.config.ROOT + self.request.path)

        call = imp(self.request.mod, self.request.controller, self.package)
        return call(self.request, *self.request.args)

