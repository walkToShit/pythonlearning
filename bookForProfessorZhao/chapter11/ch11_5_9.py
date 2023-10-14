def decoration_fun_param(func):   #创建一个装饰器
    def wrapper(*param, **param1):  # 用元组和字典 可以接收各种类型参数
        print('我是谁')
        print('我在哪')
        print('我要干什么')
        print("元组接收的参数",param,"字典接收的参数：",param1)
        func(*param, **param1)

    return wrapper


@decoration_fun_param
def test(param):
    print('----这是test调用---------', param)


@decoration_fun_param
def test1(a, b, c):
    print('----这是test1调用---------'*3)
    print('a is {}  b is{}  c is {}'.format(a, b, c))


@decoration_fun_param
def test2(param):
    print('----这是test2调用---------' * 3)
    for i in param:
        print(i)

@decoration_fun_param
def test3(*param):
    print('----这是test3调用---------' * 3)
    print(param)


list1 = ['tom', 'jack', 'candy']
test(1234)   # 单个位置传参数
test1('asd', 'das', 'asd') # 多个位置传参数
test1(a='lucy', b='candy', c='nothing') # 关键字传参数
test2(list1)           #接收列表参数
test3(*list1)     #接收可变参数