def decoration_fun(func):
    a = 100
    def wrapper():
        func()
        print('---------------刷漆----------')
        print('---------------铺地板----------', a)

    return wrapper
# 使用装饰器
#标准装饰器使用方式
@decoration_fun
def house():
    print('我是毛坯房')
house();

#一般方式
def house1():
    print('我是装修好的')

secondcall = decoration_fun(house1);
secondcall();