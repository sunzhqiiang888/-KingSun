#!/usr/bin/env python3


#  Student 类对象
class Student:

    #  类对象的属性
    name = '未知'
    age = 20
    sex = '男'


if __name__ == "__main__":
    def main():

        s = Student()   #执行类对象, 返回实例对象
        s.name = "张三"
        s.en = 34
        s1 = Student()   #执行类对象, 返回实例对象
        #  s1.name = "李四"

        print("id(s.name): ", id(s.name))
        print("id(s1.name): ", id(s1.name))
        print("id(Student.name): ", id(Student.name))

        #  Student.name = "王二"

        print("Student: ", Student.name, Student.age, Student.sex)
        print("s: ", s.name, s.age, s.sex, s.en)
        print("s1: ", s1.name, s1.age, s1.sex)

        #  s.name = "张三"
        #  s.age = 22

    main()
