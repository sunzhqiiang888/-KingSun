#!/usr/bin/env python3


def test():
    n = []
    def inner():
        nonlocal n
        print("id(n): ", id(n))
        n.append(len(n) + 1)
        return n
    return inner


if __name__ == "__main__":
    def main():
        c = test()
        print(c, type(c), callable(c))
        print("c n: ", c())
        print("c n: ", c())
        print("c n: ", c())

        d = test()
        print("d n: ", d())
        print("d n: ", d())
        print("d n: ", d())


    main()

