# 闭包

def func(a, b):
    c = 10

    def inner_func():
        nonlocal c
        c += 1  # 从这句话来看 整个方法的变量的都会保存一个新线程，c的变化没有记录到第二次调用
        s = a + b + c
        print('相加之后的值：', s)

    return inner_func


# 调用 func 两次调用 互不影响  有点java中 一个对象的方法调用 每次调用都新生成一个线程来保存数据一样
ifunc = func(6, 9)
ifunc1 = func(2, 8)
ifunc1()
ifunc()
