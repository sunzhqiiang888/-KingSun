#!/usr/bin/env python3

#  \033[       VT终端码的前缀标识


if __name__ == "__main__":
    def main():
        print("\033[?25l")
        for i in range(8):
            print("\033[%dmhello \033[%dmworld\033[%dmStyle\033[0m" % (30 + i, 40 + i, i))

        print("\033[1;31;44mhello\033[0m\033[31;44mhello\033[0m", end='')
        print("\033[s")
        print("\033[10;50HVT...", end="")
        print("\033[1AUP...", end="")
        print("\033[5BDOWN...", end="")
        print("\033[50DLEFT...", end="")

        input()
        print("\033[?25h")

        print("\033[1;1H\033[2J", end="")

        input()

        print("\033[uload...")

        input()

    main()
