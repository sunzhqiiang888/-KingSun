#!/usr/bin/env python3


def index():
    return "<h3>MVC HELLO INDEX</h3>"


def show(name="未知"):
    name = name.encode('iso-8859-1').decode('utf-8')
    return "<h3>MVC HELLO SHOW %s</h3>" % name
