# 魔术方法
'''
new  方法
 生成对象的顺序
 1.new 开辟空间 并将地址给init 中的self参数
 2.执行init方法 并进行初始化
 3.将生成好的对象返回

__call__：对象调用方法
  当对象被当做函数调用的时候此方法被调用
  p = Person('jack')
  p('对象函数式调用')

__del__:delete的缩写  析构魔术方法    不建议自己写
触发时机： 当对象没有用（没有任何变量引用）的时候被触发
1.对象赋值
   p = Person()
   p1 = p
   说明：p 和p1共同指向同一个地址
2.删除地址的引用
   del p1 删除 p1
3.查看对地址的引用次数
  import  sys
  sys.getrefcount(p)
4.当一块空间没有了任何引用空间，默认执行__del__

__str__: 打印对象名  自动触发去调用__str__ 相当于java 的toString  方法
         一定要在方法中添加return
'''
import sys


class Person:
    test = None

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def __new__(cls, *more):  # 向内存要空间
        print('------>new')
        cls.test = more  # 在new 方法可以初始化类属性
        # object.__new__(cls)
        return super().__new__(cls)

    def __call__(self, name):  # 当对象被当做函数调用的时候此方法被调用
        print('----call---')
        print('执行对象得到的参数--->', name)

    def __del__(self):
        print('----------del--------------')


p = Person('jack')
print(p.test)
print(p.name)
p1 = p
p2 = p
print(p)
print(sys.getrefcount(p))
del p2

p('对象函数式调用')
