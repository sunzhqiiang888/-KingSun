#!/usr/bin/env python3

import pygame
from pygame.locals import *

if __name__ == "__main__":
    def main():
        pygame.init()

        pygame.display.set_mode((400, 400))

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
