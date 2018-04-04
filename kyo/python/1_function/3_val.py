#!/usr/bin/env python3


def test(num):
    print("test num id: ", id(num))
    num[0] += 1
    #  num = "hello"
    print("test edit num id: ", id(num))


if __name__ == "__main__":
    def main():
        #  num = [10]
        num = {0: 10}
        print("main num id: ", id(num))
        test(num)
        print("main num = ", num)

    main()
