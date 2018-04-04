#!/usr/bin/env python3


def myrange(num):
    i = 0
    print("while start...")
    while i != num:
        print("yield %d" % i)
        yield i
        i += 1


def test():
    print("A....")
    yield 'aa'
    print("B....")
    yield 'bb'
    print("C....")
    yield 'cc'
    print("D....")
    yield 'dd'


if __name__ == "__main__":
    def main():
        #  for i in myrange(10):
            #  print(i)

        it = iter(test())
        print(next(it))
        print("----------------")
        print(next(it))
        print("----------------")
        print(next(it))
        print("----------------")
        print(next(it))

        #  it = iter(myrange(10))
        #  next(it)
        #  print("---------------")
        #  next(it)
        #  print("---------------")

        #  it = iter(myrange(10))
        #  next(it)

        #  while True:
            #  try:
                #  print(next(it))
            #  except:
                #  break

    main()
