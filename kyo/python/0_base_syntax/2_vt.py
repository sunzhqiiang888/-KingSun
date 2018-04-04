#!/usr/bin/env python3

import time
from vt import *

if __name__ == "__main__":
    def main():
        num = 50
        #  print("\033[?25l")
        #  print("\033[2J\033[1;1H[", "." * num, "]", sep='', end='', flush=True)
        #  for i in range(num):
            #  print("\033[1;%dH\033[32m#\033[0m\033[1;53H%4d%%" % (i + 2, (i + 1) * 2), end='', flush=True)
            #  time.sleep(0.1)
        #  print("\033[?25h")

        v = Vt()

        #  v.cout().hide().screen().goto().out('[%s]' % ('.' * num)).endl()
        v.run(HIDE, SCREEN, v.goto(), v.out('[%s]' % ('.' * num)))
        for i in range(num):
            v.cout().goto(c=2 + i).out('#', GREEN).goto(c=53).out("%4d%%" % ((i + 1) * 2)).endl()
            v.run()
            time.sleep(0.1)
        v.show()

    main()
