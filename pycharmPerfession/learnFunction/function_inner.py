# 内部函数
global_nonchangablevairation = 100


def fun():
    n = 100
    list1 = [3, 9, 6, 4]

    def inner_func():
        global global_nonchangablevairation
        nonlocal n  # 用于修改外部函数的不可变的变量
        for index, i in enumerate(list1):
            list1[index] = i + n
        list1.sort()
        n += 1
        global_nonchangablevairation += 100

    inner_func()
    print(list1, n, global_nonchangablevairation)


fun()
