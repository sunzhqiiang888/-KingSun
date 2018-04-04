#!/usr/bin/env python3


def test(num):
    print("test: ", num)


def hello(num):
    print("hello: ", num)


def testCall(call, num):
    #  test(num)
    call(num)


if __name__ == "__main__":
    def main():
        #  a = test
        #  a(78)
        l = lambda n: print("A: %d" % n)
        testCall(l, 100)
        testCall(lambda n: print("B: %d" % n), 100)

    main()
