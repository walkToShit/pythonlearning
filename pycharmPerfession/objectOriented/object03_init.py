#函数和类里面定义的：方法

def func(name):
    print('------->',name)

def func(names):
    for name in names:
        print(name)

namelist = ['aa','b','c']

func(namelist)

class Phone:
    #魔术方法之一:称作魔术方法   __名字__()
    def __init__(self):  #初始的  执行初始化
        self.price ='4999'
        print('-------------init')
    def call(self):
        print('-----------call')
        print('价格',self.price)#不能保证每个self中都有price  'Phone' object has no attribute 'price'

p = Phone()
p.call()

p1 = Phone()
p1.price = 5999
p1.call()

class Person:
    name ='zhangsan'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self,food):
        print('{}正在吃{},吃完了就{}岁了'.format(self.name,food,self.age))

p = Person("linzhiyi",31)
p.eat("滋味肉")
