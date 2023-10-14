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
