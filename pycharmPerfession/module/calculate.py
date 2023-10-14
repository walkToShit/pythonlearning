
__all__ = ['number','name','add','Calculate']
#变量
number = 100
name = 'calculate'
#函数
def add(*args):
    sum = 0
    if len(args) >1:
        for i in args:
            sum +=i
    else:
        print("至少传入两个参数")
    return sum

def subtract(*args):
    sum = 0
    if len(args) >1:
        pass
    else:
        print("至少传入两个参数")

def multiply(*args):
    sum = 0
    if len(args) >1:
        pass
    else:
        print("至少传入两个参数")
def divided(*args):
    sum = 0
    if len(args) >1:
        pass
    else:
        print("至少传入两个参数")


#类

class Calculate:
    def __init__(self,num):
        self.num =num

    def test(self):
        print("正在使用Calculate计算....")

    @classmethod
    def test1(cls):
        print("--------->Calculate中的类方法")

def test():
    print("我是测试--------"*5)


print('__name__:',__name__)
if __name__ =='__main__':  #可以判断是不是本模块调用 估计是测试时判断
    print(__name__)
    test()
