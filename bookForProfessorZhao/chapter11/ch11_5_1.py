msg = "我是全局变量";  # 声明一个全局变量
num = 0;


def fun():
    global num;    #通过global 声明 我即将使用的num变量是全局变量
    num = num + 1;
    print(msg);


for x in range(1, 10):
    fun();

print("fun函数的调用次数：", num)
