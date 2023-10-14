'''
  __init__.py 文件
  当导入包的时候，默认调用__init__.py 文件
  作用：
  1.当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py中
  2.此文件中函数，变量等的访问，秩序通过包名.函数的方式调用
  3.结合__all__=[通过*可以访问的模块]

'''
import objectOriented  #表示导入objectOriented__init__.py文件
from objectOriented import *
#from  模块 import *  表示可以使用模块里面的所有内容，如果没有定义__all__所有的都可以访问
#                     但是如果添加上了__all__  只有 __all__=[] 列表中可以访问的

#from 包 import * 表示该包中内容（模块）是不能访问的，就需要在__init__.py 文件中定义__all__=[可以通过*可以访问的模块]

print("module中调用。。。。"+objectOriented.name)
objectOriented.printAA()
objectOriented.testinit()
print(objectOriented.object15_singleton.s)
# print(objectOriented.__all__)
# objectOriented.__all__ = ['object10_property','object09_private']
# print(objectOriented.__all__)
# from objectOriented import *
# print(dir())