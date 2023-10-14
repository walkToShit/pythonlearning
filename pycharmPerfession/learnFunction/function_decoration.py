# 装饰器  NB

def test():
    print('------我是test----------')


def func(funcuion):
    print(funcuion)
    funcuion()
    print('----------我是func------------------')


func(test)
print("#" * 20)


def decoration_fun(func):
    a = 100

    def wrapper():
        func()
        print('---------------刷漆----------')
        print('---------------铺地板----------', a)

    return wrapper


# 使用装饰器
@decoration_fun
def house():
    print('我是毛坯房')


house()

print('含参数装饰器test---------------------------------------------')


def decoration_fun_param(func):
    def wrapper(*param, **param1):
        print('我是谁')
        print('我在哪')
        print('我要干什么')
        func(*param, **param1)

    return wrapper


@decoration_fun_param
def test(a):
    print('-------------', a)


@decoration_fun_param
def test1(a, b, c):
    print('a is {}  b is{}  c is {}'.format(a, b, c))


@decoration_fun_param
def test2(a):
    for i in a:
        print(i)


list1 = ['tom', 'jack', 'candy']

test(1234)
test1('asd', 'das', 'asd')
test1(a='lucy', b='candy', c='nothing')
test2(list1)


# 多层装饰器 谁离函数越近就先使用谁


def fun_decoration_step1(func):
    print('fun_decoration_step1', '---start')

    def wrapper():
        func()
        print('刷漆')

    print('fun_decoration_step1', '---end')
    return wrapper


def fun_decoration_step2(func):
    print('fun_decoration_step2', '---start')

    def wrapper():
        func()
        print('铺地板')

    print('fun_decoration_step2', '---end')
    return wrapper


@fun_decoration_step2
@fun_decoration_step1
def house1():
    print('我是毛坯房')


house1()


# 含有参数的装饰器
def outer(param):
    def fun_decoration_param(func):
        print('fun_decoration_param', '---start')

        def wrapper():
            func()
            print('刷漆得需要{}天'.format(param))

        print('fun_decoration_param', '---end')
        return wrapper

    return fun_decoration_param


@outer(10)
def house2():
    print('我是毛坯房2')


house2()
