def fun():
    c = 10;
    def innerfun(a,b):
        nonlocal c;
        c += 1;
        s = a+b+c;
        print("相加后的值： ",s)
    return innerfun;


func1 = fun();  # 接收返回的内部函数
print("输出返回的函数：",func1);
func1(1,1) #使用内部函数
