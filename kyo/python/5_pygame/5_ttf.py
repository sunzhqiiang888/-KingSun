#!/usr/bin/env python3

import pygame
from pygame.locals import *

if __name__ == "__main__":
    def main():
        pygame.init()

        #  font = pygame.font.SysFont("dejavusansmono", 28, True, True)
        font = pygame.font.Font("./simfang.ttf", 28)
        font.set_bold(True)
        txt = font.render("你好! Hello World...", True, (255, 255, 255))

        screen = pygame.display.set_mode((400, 400))

        screen.blit(txt, (0, 0))

        pygame.display.update()

        while True:
            e = pygame.event.wait()
            if e.type == QUIT:
                break
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE or e.key == K_q:
                    break
            #  elif e.type == MOUSEMOTION:
                #  print(e.pos)
            elif e.type == MOUSEBUTTONDOWN:
                print(e.pos, e.button)

        pygame.quit()

    main()
