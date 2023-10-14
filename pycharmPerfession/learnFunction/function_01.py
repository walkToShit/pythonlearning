# 定义函数：随机数的产生
import random


def generate_norepeatedten_random() -> set:
    numberSet = set()
    while True:
        numberSet.add(random.randint(1, 30))
        if len(numberSet) == 10:
            break
    return numberSet


def add(a, b):
    return a + b


# def add(*args)  则直接会重载函数  将上面的add 覆盖掉

# 可变参数    可变参数必须放在固定参数后面 同java def changableparam(name,*args):   *可变参数
def changableparam(*args):
    print(args)


# 参数设置默认值
def add1(a, b=10):
    return a + b


def add1(a, b=10, c=12):
    return a + b + c


# 自动装箱 变成字典 接受字典类型的关键字  **param 拆包装包方式  传参数的时候 必须是 key = value 形式  **关键字参数
def fun(**param):
    print(param)


print(generate_norepeatedten_random)  # 这是函数声明后所在地址
print(generate_norepeatedten_random())
print(add(1, 2))
print(isinstance(2, int))  # 和java 的instance of 是一样的
changableparam()
changableparam(1, 2)
changableparam(1, 2, 3, 4, 5, 6)
tuple_01 = {'w', 's', 'x', 'c', 'f', 'r', 'h'}
changableparam(*tuple_01)  # 元组的拆包  封包  可变参数传元组的拆包
print(add1(1, 2))
print(add1(1))
#  可以明确给第几个参数赋值
print(add1(1, c=2))
#  关键字参数
fun(a=1, b=2, c=3)
dict1 = {'1': 2, '2': 3, '3': 4}
# dict1 = {1: 2, 2: 3, 3: 4}  #TypeError: keywords must be strings
fun(**dict1)  # 3.5以后的拆包方式


def fun1(a, b=10, *param):
    print(a, b, param)


# fun1(1,20,a=1,b=2) TypeError: fun1() got multiple values for argument 'a'
# 当关键字赋值 和 参数赋值冲突的时候  参数赋值是优先的  1给了a  后面a=1 还是给a赋值  故报错

# 多个返回值 自动封包为元组
def returntest():
    return 'a', 'b', 'c'


# 返回多个值，也可以多个接
x, y, z = returntest()
print(x, y, z)
print(returntest())
