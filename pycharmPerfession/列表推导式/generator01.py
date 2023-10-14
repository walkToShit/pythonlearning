'''



得到生成器的方式
1.通过列表推导式得到生成器
'''

#[0,3,6,9,12,15,18,21,24,27....]
#此种方式一次性就开辟了空间
from functools import reduce

newlist = [x*3 for x in range(20)]
print(newlist)

#得到生成器    注意不是推导元组 是生成器
g=(x*3 for x in range(20))
print(g)
#方式一： 通过调用_next_() 方式得到元素
print(g.__next__())
#方式二： next()
print(next(g))



