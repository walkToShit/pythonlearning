msg = "我是全局变量";       #声明一个全局变量
num = 0;
num2 = 10
def fun():
    global num ;
    num  = num +1;
    nonlocal  num2;
    num = num-1;
    print(msg);


for x in range(1,20):
    fun();

print("fun函数的调用次数：",num)
print("第二种方式函数调用全局变量nonlcal：",num)