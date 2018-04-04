#!/usr/bin/env python3

from term  import Term

if __name__ == "__main__":
    def main():
        gt = Term()

        while True:
            ch = gt.get()

            if ch == 'q':
                break
            elif ch == 'w':
                print('\033[1A', end='', flush=True)
            elif ch == 's':
                print('\033[1B', end='', flush=True)
            elif ch == 'a':
                print('\033[1D', end='', flush=True)
            elif ch == 'd':
                print('\033[1C', end='', flush=True)
            elif ch == 'c':
                print('\033[2J', end='', flush=True)
            else:
                print(ch, end='', flush=True)

        gt.exit()



    main()
