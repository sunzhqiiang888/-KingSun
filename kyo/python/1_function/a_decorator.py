#!/usr/bin/env python3

def p(func):
    def inner(s):
        return '<p>' + func(s) + '</p>'
    return inner

def tag(*args, name='p', **kwargs):
    def _tag(func):
        def inner(*args, **kwargs):
            return '<%s>%s</%s>' % (name, func(*args, **kwargs), name)
        return inner
    return _tag


@tag(name='html')
@tag(name='body')
@tag(name='div')
@tag()
#  @p
def text(s):
    return '<span>%s</span>' % s

@tag(name='p')
def hello(s):
    return "hello %s" % s

#  @tag(name="div")
#  def text():
#  以上两行代码相当于: text = tag(name='div')(text)

#  @p
#  def text()
#  以上两行代码相当于: text = p(text)

if __name__ == "__main__":
    def main():
        print(tag(name='div')(hello)('Decorator'))
        print(text("hello world"))

    main()
