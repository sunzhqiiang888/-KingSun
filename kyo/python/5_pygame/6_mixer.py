#!/usr/bin/env python3

import pygame
from pygame.locals import *

if __name__ == "__main__":
    def main():
        pygame.init()

        pygame.display.set_mode((400, 400))

        #  print(pygame.mixer.music.get_busy())
        bom = pygame.mixer.Sound("./bom.wav")
        #  pygame.mixer.music.load("./God.mp3")
        #  pygame.mixer.music.play()

        while True:
            e = pygame.event.wait()
            if e.type == QUIT:
                break
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE or e.key == K_q:
                    break
            elif e.type == MOUSEBUTTONDOWN:
                bom.play()
                pass

        pygame.quit()

    main()
