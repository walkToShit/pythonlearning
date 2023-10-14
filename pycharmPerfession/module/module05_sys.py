'''
当你导入一个模块，python解析器对模块位置的搜索顺序是：
1.当前目录
2.如果不在当前目录,python则搜索在shell 变量PYTHONPATH下的每个目录。
3.如果找不到，python会查看默认路径。unix下，默认路径一般为/uer/local/lib/python
模块搜索路径存储在system模块的sys.path变量中。变量包含当前目录，PYTHONPATH和有安装过程
决定的默认目录。

'''
import sys

'''
自定义模块
系统模块
'''

print(sys.path) #导入模块 搜索模块的路径
print(sys.version)
print(sys.argv)  #运行程序时得到一些参数， 相当于java 中main函数中 String[]args 传参数