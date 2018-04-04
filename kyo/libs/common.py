#!/usr/bin/env python3

def repeat(code, *args, itype=str, seq=None, prompt="请输入: ",
           quitCh='q', **kwargs):
    """
    重复测试
    """
    if not callable(code):
        return None

    while True:
        inputList = input(prompt)
        if not inputList:
            continue

        if inputList == quitCh:
            break

        if seq is not None:
            inputList = [itype(x) for x in inputList.strip(seq).split(seq)]
        else:
            inputList = [itype(inputList)]

        ret = code(*inputList, *args, **kwargs)
        if ret:
            return ret

def menu(menulist, cmdlist):
    """
    实现简单菜单
    """
    menuCount = len(menulist)

    while True:
        for i, l in enumerate(menulist, 1):
            print("%2d. %s" % (i, l))
        print(" 0. 退出")
        s = input("请输入[0 - %d]: " % menuCount)
        if s == "0":
            break

        try:
            cmdlist[int(s) - 1]()
        except Exception as e:
            print("\033[31;1m----> %s\033[0m" % e)

