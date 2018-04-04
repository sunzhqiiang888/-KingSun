#!/usr/bin/env python3

import pygame
from random import randint, choice
from pygame.locals import *
from threading import Thread
import time


class Ball:

    def __init__(self, W, H, **kwargs):
        self.r = kwargs.get('r', randint(5, W // 6))
        self.x = kwargs.get('x', randint(self.r + 1, W - self.r - 1))
        self.y = kwargs.get('y', randint(self.r + 1, H - self.r - 1))
        self.x_inc = kwargs.get('x_inc', choice((-3, 3)))
        self.y_inc = kwargs.get('y_inc', choice((-3, 3)))
        self.color = kwargs.get('color', (randint(0, 255),
                                          randint(0, 255),
                                          randint(0, 255)))
        self.__dict__.update(kwargs)

    @staticmethod
    def create(w, h, num=1):
        return [Ball(w, h) for i in range(num)]


class BallPro:

    def __init__(self, w=640, h=480, num=1):
        """
        弹球程序主类构造方法
        """
        self.w = w
        self.h = h
        self.pause = False
        self.quit = False
        pygame.init()
        self.screen = pygame.display.set_mode((w, h))
        self.ball = Ball.create(w, h, num)
        self.circle = pygame.draw.circle

    def keyHandle(self, key):
        """
        键盘按键事件处理
        """
        if key in (K_ESCAPE, K_q):
            return True
        elif key == K_w:
            for b in self.ball:
                b.y_inc = -1 * abs(b.y_inc)
        elif key == K_s:
            for b in self.ball:
                b.y_inc = abs(b.y_inc)
        elif key == K_a:
            for b in self.ball:
                b.x_inc = -1 * abs(b.x_inc)
        elif key == K_d:
            for b in self.ball:
                b.x_inc = abs(b.x_inc)
        elif key == K_SPACE:
            self.pause = not self.pause


    def mouseHandle(self, pos, button):
        """
        鼠标事件处理
        """
        if 0 <= pos[0] <= 100 and 0 <= pos[1] <= 100:
            pygame.draw.circle(self.screen, (255, 255, 0), (200, 200), 50, 10)
            pygame.display.update()

    def event(self):
        """
        事件处理主框架
        """
        while True:
            e = pygame.event.wait()
            if (e.type == QUIT
                or (e.type == KEYDOWN and self.keyHandle(e.key))
                or (e.type == MOUSEBUTTONDOWN
                    and self.mouseHandle(e.pos, e.button))):
                break
        self.quit = True

    def draw(self):
        """
        在窗口画所有球
        """
        for b in self.ball:
            self.circle(self.screen, b.color, (b.x, b.y), b.r)

    def move(self):
        """
        所有球的移动判断
        """
        def _move(b):
            if b.x + b.x_inc - b.r <= 0 or b.x + b.r + b.x_inc >= self.w - 1:
                b.x_inc = -b.x_inc

            if b.y + b.y_inc - b.r <= 0 or b.y + b.r + b.y_inc >= self.h - 1:
                b.y_inc = -b.y_inc

            b.x += b.x_inc
            b.y += b.y_inc

        for b in self.ball:
            _move(b)

    def run(self):
        """
        球的移动动画
        """
        while not self.quit:
            if not self.pause:
                self.screen.fill((0, 0, 0))
                self.draw()
                self.move()
                pygame.display.update()
            time.sleep(0.03)

    def do(self):
        """
        开线程实现球的移动动画和处理窗口事件
        """
        Thread(target=self.run, daemon=True).start()
        self.event()

    def __del__(self):
        """
        对象销毁时自动调用
        """
        pygame.quit()


if __name__ == "__main__":
    def main():
        BallPro(num=10).do()

    main()
