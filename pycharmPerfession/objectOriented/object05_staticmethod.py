# 静态方法
'''
静态方法：很类似 类方法
 1.需要装饰器 @staticmethod
 2.静态方法无需传递参数
 3.只能访问类的属性和方法，对象是无法访问的
 4.加载实际同类方法

 总结 类方法和静态方法:
 不同：
 1.装饰器不同
 2.类方式是有参数的，静态方法没有参数

 相同：
 1.只能访问类的属性和方法，对象是无妨访问的
 2.都可以通过类名调用访问
 3.都可以在创建对象之前使用，因为是不依赖于独享

 普通方法与两者的区别
 不同：
 1.没有装饰器
 2.普通方法是要依赖对象，因为每个普通方法都有一个self
 3.只有创建对象才可以调用普通方法，否则无法调用

'''
class Person:
    __age = 18
    def __init__(self,name):
        self.name =name

    @classmethod
    def updateAge(cls, age):
        cls.__age = 20
    @staticmethod
    def test(s):
        Person.updateAge(12)
        print('------------>静态方法',s)
        print(Person.__age)

Person.test("a")