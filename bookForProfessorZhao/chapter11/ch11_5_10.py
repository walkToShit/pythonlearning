def outer(param):
    def fun_decoration_param(func):
        print('fun_decoration_param', '---start')

        def wrapper():
            func()
            print('刷漆得需要{}天'.format(param))

        print('fun_decoration_param', '---end')
        return wrapper

    return fun_decoration_param     #将装饰器作为返回值返回


@outer(10)
def house2():
    print('我是毛坯房2')


house2()