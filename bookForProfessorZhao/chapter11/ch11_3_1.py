def function1(num):
    '''返回传入参数的3倍'''
    print("我是function1");
    return num*3;


rmg1 = function1(3); #function1 接收的返回变量
print("function1返回的值是 ：",rmg1 , "数据类型：",type(rmg1));
