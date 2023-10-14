global_nonchangablevairation = 100;


def fun():  # 外层嵌套函数
    n = 100
    list1 = [3, 9, 6, 4]

    def inner_func():  # 内层嵌套函数
        global global_nonchangablevairation;
        nonlocal n;  # 用于修改外部函数的不可变的变量
        for index, i in enumerate(list1):
            list1[index] = i + n
        list1.sort()
        n += 1
        global_nonchangablevairation += 100  # 在哪里修改则在对应的嵌套位置顶层声明global

    inner_func()  # 外层调用内嵌函数
    print("列表：", list1, " 外层变量n的值为：", n, " 全局变量的值为：", global_nonchangablevairation)


fun();
