#可迭代对象：1.生成器2.元组  列表 集合 字典 字符串
#如何判断一个对象是否可迭代
from typing import Iterable

list1 = [1,2,3,4,5,6]

f = isinstance(list1,Iterable)
print(f)
g=(x*3 for x in range(20))
print(type(g))
iter(list1)

print(next(list1))
'''
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，知道所有的元素被访问完结束。
迭代器只能往前不会后退
可以被next()函数调用兵不断返回下一个值的对象称为迭代器：iterator
生成器是可迭代的  也是迭代器
list 是可迭代的  但是不是迭代器
'''

'''
生成器和迭代器:


'''
