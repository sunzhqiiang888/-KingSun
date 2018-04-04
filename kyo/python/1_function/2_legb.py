#!/usr/bin/env python3

list = 'Global My List'

def test():
    list = 'Test My List'

    def inner():
        #  nonlocal list    #声明变量为外部函数定义
        global list         #声明变量为全局定义
        #  list = 'inner My List'
        print("list = %s" % list)
        list = "Inner Edit List"

    inner()
    print("Test Out List: %s" % list)


if __name__ == "__main__":
    def main():
        test()

    main()
    print("Global Out List: %s" % list)
