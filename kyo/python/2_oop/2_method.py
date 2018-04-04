#!/usr/bin/env python3


class Student:

    #  def __init__(self, name, age, sex, phone):
        #  self.name = name
        #  self.age = age
        #  self.sex = sex
        #  self.phone = phone

    def __init__(self, name='未知', age='20', sex='男', phone='110', **kwargs):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone
        self.__dict__.update(kwargs)

    def __str__(o):
        s = "姓名: %s, 性别: %s, 年龄: %s, 电话: %s"
        s = s % (o.name, o.sex, o.age, o.phone)
        s += '\n\t额外的数据: \n'
        for k, v in o.__dict__.items():
            if k in ['name', 'sex', 'age', 'phone'] or k.startswith('__'):
                continue
            s += "\t%s: %s\n" % (k, v)
        return s

    def run(self):
        print("running....")


    def __int__(self):
        return 9999

    def __iter__(self):
        return iter(self.name)

    def __next__(self):
        for c in self.name:
            yield c

    @staticmethod
    def static():
        print("static Test....")

    @classmethod
    def cm(cls):
        print("class method test.....", cls)


if __name__ == "__main__":
    s = Student("张三", 17, '男', '110')
    print(s)

    print(Student())
    print(Student(age=999, zh='...', start=99, end=199))
    print(Student("李四"))
    print(Student("李四", 30))
    print(Student("李小四", 30, '女'))
    print(Student("李小四", 30, '女', '119'))
    print(Student("李小四", 30, '女', '119', en=34, cn=455))

    print(int(s))
    print(list(s))

    s.run()
    Student.run(s)

    s.static()
    Student.static()
    s.cm()
    Student.cm()

    #  s1 = Student.init("李四", 18, '女', '119')

    #  s.show()
    #  s1.show()

