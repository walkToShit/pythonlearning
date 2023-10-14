# global 变量的范围
# 局部变量  全局变量

# 声明在方法外的叫全局变量  所有函数都可以访问
# 声明在方法内的叫局部变量
# 当方法要修改全局变量的时候 需要声明 global  相当于java 中 this.name = 'dsadsa'
# 当全局变量是可变类型 则不需要声明global   若是不可变的则需声明global
name = 'dsadsa'
list1 = [1, 2, 3, 4, 5]


def testvairation():
    global name
    name += '3213'


def testvairation1():
    name = 'linzhiyi'
    name += '3213'
    print(name)


def testvairation2():
    print(name)


def upadtelist():
    list1.append(6)


testvairation1()
testvairation()
print(name)
upadtelist()
print(list1)
