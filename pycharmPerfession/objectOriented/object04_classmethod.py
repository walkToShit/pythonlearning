#类方法
'''
特点：
 1.定义需要依赖装饰器@classmethod
 2.类方法参数不是一个对象，而是类
 3.只能调用类属性
 4.类方法中课
类方法的作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些功能或是动作

'''
class Dog:
    __age= 18
    def __init__(self,nikename):
        self.nikename = nikename

    def run(self):
        print('{}在院子里抛开跑去！'.format(self.nikename))

    def eat(self):
        print('吃饭。。。')
        self.run() #类中方法的调用，需要通过self.方法名()
    def show(self):
        print('--------------->',Dog.age)

    @classmethod
    def updateAge(cls,age):
        cls.__age = 20
    @classmethod
    def show_age(cls):
        print('age----------->',cls.__age)

    @classmethod  #所以类方式不能还用对象方法
    def test(cls):#cls class 的意思
        print(cls)
        print(cls.nikename)
Dog.updateAge(20)
Dog.show_age()

d = Dog('大黄')
d.run()
d.test()


