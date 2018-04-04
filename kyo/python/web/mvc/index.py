#!/usr/bin/env python3


import os
import sys

CONFIG = {
    'ROOT': os.getcwd(),
    'DEBUG': True,
    'LOG_FILE': '/tmp/mvc.log',
    'APP_LIST': ['blog'],
    'DEFAULT': {
        'APP': 'blog',
        'CONTROLLER': 'index',
        'METHOD': 'index',
        'ERROR': '非法操作....',
    },
    'NAME': {
        'CONTROLLER': 'controller',
        'VIEW': 'view',
        'MODEL': 'model',
        'CONF': 'configs',
        'STATIC': 'static',
    },
    'TEMPLATE_SUFFIX': 'html',
}

sys.path.append(CONFIG['ROOT'] + '/core')

from mvc import MVC

application = MVC(CONFIG)


if __name__ == '__main__':
    import sys
    from wsgiref.simple_server import make_server

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

    make_server('0.0.0.0', port, application).serve_forever()

