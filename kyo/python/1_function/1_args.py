#!/usr/bin/env python3


def test(name='未知', age=17, sex='男', phone="13602578723"):
    print("学生信息: %s(%d) %s %s" % (name, age, sex, phone))


def testV(name, *args, phone="13877777777", **kwargs):
    #  print(args, type(args), kwargs, type(kwargs))
    print(name, args, phone, kwargs)


if __name__ == "__main__":
    def testArgs():
        test()
        test("李四")
        test("张三", 23)
        test("王二", 17, '女')
        test("马六", 19, '未知', '13877669900')

        test("李小四", phone='110')
        test(phone='119')

    def testVargs():
        #  testV()
        testV("李四")
        testV("张三", 23, en=34, cn=56)
        testV("王二", 17, '女')
        testV("马六", 19, '未知', '13877669900')
        testV("李小四", phone='110')
        testV("王五", phone='119')

    testVargs()
