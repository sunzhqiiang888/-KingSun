#!/usr/bin/env python3


from core.mvc import MVC


def index():
    return "<h1>Hello Index</h1>"


application = MVC()


if __name__ == '__main__':
    import sys
    from wsgiref.simple_server import make_server

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

    make_server('0.0.0.0', port, application).serve_forever()



