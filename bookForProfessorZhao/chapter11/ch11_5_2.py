def fun():
    msg = "我是局部变量" ;   # 声明一个局部变量
    print(msg);


fun();
#print(msg)     # 在变量作用域范围外（函数外）使用局部变量则报错