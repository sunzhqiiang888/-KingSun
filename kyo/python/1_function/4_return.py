#!/usr/bin/env python3


def add(a, b):
    if a < 0 or b < 0:
        return 0
    return a + b


if __name__ == "__main__":
    def main():
        print(add(add(add(add(3, 5), 10), 10), 10))

        r = add(30, 50)
        print("r = ", r, add(6, 8))

    main()
