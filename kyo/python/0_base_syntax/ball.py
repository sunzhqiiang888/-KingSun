#!/usr/bin/env python3

import time
import sys
from random import randint, choice
from vt import *
from term import *

W = 50
H = 15
v = Vt()
gt = Term()
pause = False

class Ball:

    def __init__(self, **kwargs):
        self.r = kwargs.get('r', randint(2, H - 1))
        self.c = kwargs.get('c', randint(2, W - 1))
        self.r_inc = kwargs.get('r_inc', choice((-1, 1)))
        self.c_inc = kwargs.get('c_inc', choice((-1, 1)))
        self.ch = kwargs.get('ch', choice('@0123456789ABCDEF'))
        self.color = kwargs.get('color', v.get())
        self.__dict__.update(kwargs)

    @staticmethod
    def create(num=1):
        return [Ball() for i in range(num)]



def init():
    v.goto(back=False)
    for i in range(H):
        for j in range(W):
            if i == 0 or j == 0 or i == H - 1 or j == W - 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()

def draw(ball):
    for b in ball:
        v.cout().goto(b.r, b.c).out(b.ch, b.color).endl()

def move(ball):
    def _move(b):
        if b.r + b.r_inc <= 1 or b.r + b.r_inc >= H:
            b.r_inc = -b.r_inc

        if b.c + b.c_inc <= 1 or b.c + b.c_inc >= W:
            b.c_inc = -b.c_inc

        b.r += b.r_inc
        b.c += b.c_inc

    for b in ball:
        _move(b)

def ball_init(num=1):
    v.hide()
    v.cout().goto(H + 1).out("按'q'结束程序...").endl()
    return Ball.create(num)

def ball_exit():
    v.show()
    v.goto(H + 2, back=False)
    gt.exit()


def ball_run(ball):
    while True:
        if not pause:
            init()
            draw(ball)
            move(ball)
        time.sleep(0.1)

if __name__ == "__main__":
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    ball = ball_init(num)

    gt.run(ball_run, args=(ball, ))

    while True:
        ch = gt.get()
        if ch == 'q':
            break
        elif ch == 'w':
            for b in ball:
                b.r_inc = -1
        elif ch == 's':
            for b in ball:
                b.r_inc = 1
        elif ch == 'a':
            for b in ball:
                b.c_inc = -1
        elif ch == 'd':
            for b in ball:
                b.c_inc = 1
        elif ch == 'g':
            for b in ball:
                b.r_inc = choice([-1, 1])
                b.c_inc = choice([-1, 1])
        elif ch == ' ':
            pause = not pause
        elif ch == 'c':
            for b in ball:
                b.color = v.get()

    ball_exit()


