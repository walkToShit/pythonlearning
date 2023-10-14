from functools import reduce    #由于reduce 不是内建函数需要导入
tuple1 = (1, 2, 5, 3, 2, 1)
result2 = reduce(lambda x, y: x + y, tuple1)
print('------reduce-------',result2)