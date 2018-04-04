#!/usr/bin/env python3


import time


class BException(Exception):
    pass


class AException(Exception):
    pass


def C(num):
    print("C start...")
    if num > 50:
        #  raise Exception
        raise Exception("超过C函数的限制...")
    time.sleep(1)
    print("C end....")
    return num + 30

def B(num):
    print("B start...")
    #  if num > 100:
        #  raise BException()
    assert num <= 100, "B函数出错了"
    ret = C(num + 20)
    print("B end...")
    return ret

def A(num):
    print("A start...")
    if num < 0:
        raise AException()
    r = B(num + 10)
    print("A end...")
    return r


if __name__ == "__main__":
    def main():
        try:
            A(int(input("请输入: ")))
        except AException as e:
            print("不支持负数...")
        except BException as e:
            print("B函数的参数不能超过50...")
        except AssertionError as e:
            print("断言异常: ", e)
        except Exception as e:
            print("其它的异常: ", e)
        else:
            print("没有异常的情况执行代码块...")
        finally:
            print("不管有没有异常都会执行的代码块...")

    main()

