#!/usr/bin/env python3


def imp(mod, method=None, package=None):
    """
    封装导入模块或方法
    """
    if package is None:
        m = __import__(mod)
    else:
        path = package + '.' + mod
        m = __import__(path)
        for name in path.split('.')[1:]:
            m = getattr(m, name)

    if method is None:
        return m
    return getattr(m, method)







