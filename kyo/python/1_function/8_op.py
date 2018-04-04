#!/usr/bin/env python3


import glob


def handler(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 // n2
    elif op == '%':
        return n1 % n2
    elif op == '^':
        return n1 ** n2

def add(n1, n2):
    return n1 + n2;

def sub(n1, n2):
    return n1 - n2;

def mul(n1, n2):
    return n1 * n2;

def div(n1, n2):
    return n1 // n2;

def mod(n1, n2):
    return n1 % n2;

def power(n1, n2):
    return n1 ** n2;

if __name__ == "__main__":
    def main():
        #  ch = ['+', '-', '*', '%', '/', '^']
        #  op = [add, sub, mul, div, mod, power]

        #  op = {
                #  '+': lambda a, b: a + b,
                #  '-': lambda a, b: a - b,
                #  '*': lambda a, b: a * b,
                #  '/': lambda a, b: a // b,
                #  '%': lambda a, b: a % b,
                #  '^': lambda a, b: a ** b,
             #  }

        op = {}
        for filename in glob.glob("ext/*.py"):
            filename = filename.rstrip(".py")
            dictname = filename.split('/')[1]
            m = __import__("ext.%s" % dictname)
            m = getattr(m, dictname)
            op.update(m.op)
            #  print(m.op)

        for i in op:
            for j in op:
                if op[i](op[j](5, 3), 2) == 4:
                    print("(5 %s 3) %s 2 = 4" % (j, i))

    main()
