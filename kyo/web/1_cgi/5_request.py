#!/usr/bin/env python3


import os
import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


print("Content-Type: text/html; charset=utf-8\n")



#  for e in os.environ:
    #  print("<h3>%s: %s</h3>" % (e, os.environ[e]))

f = open('./boostrap.html')

print(f.read())

f.close()

print("中文")
