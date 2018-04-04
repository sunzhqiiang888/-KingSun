#!/usr/bin/env python3

import win

def quit(args):
    print("窗口退出执行的窗口, args = ", args)

def bg(k, screen):
    screen.fill(win.getColor())
    win.flip()

def btnCall(button, pos, screen):
    print("点击....")

if __name__ == "__main__":
    def main():
        pg = win.create(w=640, h=480, quitKey=win.K_q, quitCall=quit, quitCallData=(11, 22, 33, 44))
        #  pg['quitKey'] = K_z

        screen = win.screen()
        btn_pos = (100, 100, 100, 30)
        win.rect(screen, win.toColor(0xFF0000), btn_pos, 5)
        win.flip()

        win.key(pg, win.K_c, bg, screen)
        win.mouse(pg, btnCall, btn_pos, screen)

        win.loop(pg)


    main()
