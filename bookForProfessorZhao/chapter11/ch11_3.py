def function1():
    print("我是function1");

def function2():
    print("我是function2");
    return None;

rmg1 = function1(); #function1 接收的返回变量
rmg2 = function2(); #function2 接收的返回变量

print("function1返回的值是 ：",rmg1 , "数据类型：", type(rmg1));
print("function2 返回的值是：",rmg2 , "数据类型：", type(rmg2));