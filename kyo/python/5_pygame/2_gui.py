#!/usr/bin/env python3

import pygame
from random import randint
from pygame.locals import *

def triangle(dst, x, y, b, color):
    for i in range(b):
        for j in range(i):
            dst.fill(color, (x + j, y + i, 1, 1))

def circle(dst, x, y, r, color):
    for i in range(y - r, y + r + 1):
        for j in range(x - r, x + r + 1):
            if (x - j) ** 2 + (y - i) ** 2 <= r * r:
                dst.fill(color, (j, i, 1, 1))


if __name__ == "__main__":
    def main():
        pygame.init()

        screen = pygame.display.set_mode((400, 400))

        while True:
            e = pygame.event.wait()
            if e.type == QUIT:
                break
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE or e.key == K_q:
                    break
            elif e.type == MOUSEBUTTONDOWN:
                if 0 <= e.pos[0] <= 100 and 0 <= e.pos[1] <= 100:
                    screen.fill((255, 255, 0x71), (0, 0, 100, 100))
                    #  screen.fill((randint(0, 255), 0x5A, 0x71), (100, 100, 1, 1))
                    #  triangle(screen, 100, 100, 100, (255, 255, 0))
                    #  circle(screen, 200, 200, 50, (255, 255, 0))
                    pygame.draw.circle(screen, (255, 255, 0), (200, 200), 50, 10)
                    pygame.draw.ellipse(screen, (255, 255, 0), (100, 300, 100, 50))

                    pygame.display.update()


        pygame.quit()

    main()
