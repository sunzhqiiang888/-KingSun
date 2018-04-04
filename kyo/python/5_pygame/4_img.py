#!/usr/bin/env python3

import pygame
import time
from pygame.locals import *

if __name__ == "__main__":
    def main():
        pygame.init()
        screen = pygame.display.set_mode((640, 480))

        bg = pygame.image.load("./backGround.bmp")
        bg = pygame.transform.scale(bg, screen.get_size())

        img = pygame.image.load("./player.bmp")
        img.set_colorkey((247, 0, 255))
        player = []
        for i in range(11):
            player.append(img.subsurface((0, i * 48, 48, 48)))

        #  screen.blit(bg, (0, 0), (300, 300, 400, 400))
        screen.blit(bg, (0, 0))
        #  screen.blit(img, (0, 0), (0, 0, 48, 48))
        #  screen.blit(img, (100, 0), (0, 48, 48, 48))
        #  screen.blit(img, (200, 0), (0, 96, 48, 48))
        screen.blit(player[0], (0, 0))
        #  player[1] = pygame.transform.rotate(player[1], 50)
        screen.blit(player[1], (100, 0))
        player[5].set_alpha(100)
        screen.blit(player[5], (200, 0))

        pygame.display.update()


        a = 0
        n = 0
        y = 0

        while True:
            e = pygame.event.wait()
            if e.type == QUIT:
                break
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE or e.key == K_q:
                    break
                if e.key == K_SPACE:
                    while True:
                        screen.blit(bg, (0, 0))
                        new = pygame.transform.rotate(player[1], a)
                        a += 10
                        screen.blit(new, (0, 0))
                        pygame.display.update()
                        time.sleep(0.1)
                        if a >= 360:
                            a = 0
                            break

            elif e.type == MOUSEBUTTONDOWN:
                screen.blit(bg, (0, 0))
                screen.blit(player[n], (230, y))
                n = 0 if n else 1
                y += 5
                pygame.display.update()




        pygame.quit()

    main()
