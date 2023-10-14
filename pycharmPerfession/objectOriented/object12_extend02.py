'''
继承：
   Student,employee,Doctor---->都属于人类
   相同代码---》代码冗余，可读性不搞

   相同代码提取---》Person类
   Student，Employee，Doctor----》继承Person
   继承格式：
     class Student(Person):
               pass
特点：
    1.如果类中不定义__init__(),调用父类的__init__()
    2.如果子类有自己的__init__()，也需要在自己init（）中调用父类的__init__()
    3.如何调用父类__init__()：
        （1）super().__init__([参数])
         (2)super(类名, 对象).__init__([参数])    注：类名指的是当前初始化的类
    4.python 中有重写，若是子类重写了父类的方法，则子类对象调用的就是子类方法
    5.调用父类的方法： 同3
      在执行环境：super(Student,s).eat()
      在方法中  可直接 super().eat()   因为方法中已经指定了对象

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print(self.name+'正在跑步。。。。')
    def eat(self):
        print(self.name + '正在吃饭。。。。')


class Student(Person):
    def __init__(self, name, age, clazz):
        super(Student, self).__init__(name, age)
        self.clazz = clazz
    def study(self,course):
        print('{}班的学生{}，正在学{}'.format(self.clazz,self.name,course))
    def eat(self):
        print(self.name+'喜欢吃狮子头')

class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients

s =Student('jack',18,'一班')
s.run()
s.study("python基础")
s.eat()
super(Student,s).eat() #调用父类方法


e = Employee('tom',23,10000,'king')
e.run()
patients = ['司马渣','司空信','李四']
d = Doctor('lucy',30,patients)
d.run()