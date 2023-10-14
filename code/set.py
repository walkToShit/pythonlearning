#set 的声明方式  {} 默认是字典  空集合只能用set() 方式创建
##不会有重复元素 java 一样
s1 = set()
s2 = {1,2,2}
print(type(s1))
print(type(s2))
print(s2)
# 添加  add() 会将元素拆开来添加  update()  会将整个变量作为元素添加
t1 = ('hh','gg')
s2.add(t1)
print(s2)
s2.update(t1)
print(s2)
print('---------------------------------------------------')
#删除  按元素删除  删除不到报错
s2.remove(t1)
print(s2)
#删除  按元素删除  不会报错
s2.discard(t1)
print(s2)
#随机删除  如果空集合调用报错
s2.pop()
print(s2)
# 清空集合
s2.clear()
print(s2)
# +  * set不支持  支持- &
# - 是差集的意思  difference()
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,6,7}
print(set1-set2)
print(set2-set1)
print(set1.difference(set2))
print(set2.difference(set1))
# &是 交集的意思   intersaction()
print(set1&set2)
print(set1.intersection(set2))
# |  是并集的意思  union()
print(set1|set2)
print(set1.union(set2))
