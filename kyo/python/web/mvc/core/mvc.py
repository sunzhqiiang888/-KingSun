#!/usr/bin/env python3


from config import Config
from request import Request
from route import Route
from exception import MVCException


class MVC:
    def __init__(self, config):
        self.config = Config(**config)

    def response(self, response):
        self.wsgi_response(response.status, response.header)
        return [response.body]

    def do(self, env):
        request = Request(env)
        route = Route(request, self.config)
        return route.dispatch()

    def __call__(self, env, start_response):
        self.wsgi_response = start_response
        try:
            return self.response(self.do(env))
        except:
            return self.response(MVCException.do())

