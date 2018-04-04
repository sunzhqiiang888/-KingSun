#!/usr/bin/env python3


def math(s):
    stack = []
    m = dict([x for x in ")( ][ }{ ><".split()])
    for c in s:
        if c in '([{<':
            stack.append(c)
        elif c in ')]}>':
            try:
                l = stack.pop()
            except:
                return "缺少左括号!"

            if m[c] != l:
                return "左右不匹配!"
            #  if (c == ')' and l != '('
                    #  or c == ']' and l != '['
                    #  or c == '}' and l != '{'
                    #  or c == '>' and l != '<'):
                #  return "左右不匹配!"
    if len(stack) != 0:
        return "缺少右括号!"

    return s


if __name__ == "__main__":
    def main():
        print(math(input("请输入: ")))

    main()
