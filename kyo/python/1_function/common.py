#!/usr/bin/env python3


def repeat(code, *args, itype=None, seq=' ', prompt="请输入: ",
           quitCh='q', **kwargs):
    if not callable(code):
        return None

    while True:
        inputList = input(prompt)
        if not inputList:
            continue

        if inputList == quitCh:
            break

        if itype is not None:
            inputList = [itype(x) for x in inputList.strip(seq).split(seq)]

        ret = code(inputList, *args, **kwargs)
        if ret:
            return ret


def outNum(num, bit=16):
    def _outNum(num, bit):
        if not num:
            return ''
        return _outNum(num // bit, bit) + '0123456789ABCDEF'[num % bit]

    if num == 0:
        return '0'
    elif num < 0:
        prefix = '-'
        num = abs(num)

    prefix = {2:'0b', 8:'0o', 16:'0x'}.get(bit, '')

    return prefix + _outNum(num, bit)


def test():
    call = lambda a: True if a[0] == 34 else print(outNum(*a))

    repeat(call, prompt="请输入(数字 进制): ",
           itype=int)
    #  "%d %s %x %o %% %c %f"
    #  print("%#x %#o" % (100, 100))


#  print("COMMON: ", __name__)
if __name__ == "__main__":
    test()

