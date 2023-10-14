'''

在python中，模块时代吗最值的一种方式，把功能相近的函数方法哦一个文件中，一个文件（.py）就是一个模块（module）
模块名就是文件名去掉后缀py，这样做的好处是：


     --提高代码的可服用，课维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
     --解决了命名冲突，不同模块中相同的明敏不会冲突

1.自定义一些模块
2.使用系统的模块

调用其他模块的方式:
  1.import 模块名
  2.from 模块名 import 变量 函数 类 (多个导入 逗号间隔)
  3.from 模块名 import *  该模块内容全部导入
    单数如果想限制获取的内容， 可以在该模块中 设置属性__all__ = []
  4.无论是import还是from的形式，都会将模块内容进行加载
    如果不希望进行调用。就会用到__name__
    在自己的模块里面__name__ 的值是__main__
    如果在其他模块中通过导入的方式调用的话：__name__的值是：模块名
'''

# import calculate
from calculate import *  #add,number,Calculate
#包的导入  from 后面就是包名.模块名  import 后面是 模块名或是 变量 函数 类

from objectOriented.object15_singleton import Singleton
singletong = Singleton()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 使用模块中的函数  模块名.变量 函数  类
# sum1 = calculate.add(*list1)
# print(sum1)
# # 使用模块的变量
# print(calculate.name)
# # 使用模块中的类
# cal = calculate.Calculate(88)
# cal.test()
# calculate.Calculate.test1()


sum1 = add(*list1)
print(sum1)
# 使用模块的变量
print(number)
# 使用模块中的类
cal = Calculate(88)
cal.test()
Calculate.test1()

print(dir())