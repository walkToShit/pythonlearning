# 匿名函数：简化函数定义
# 格式： lambda 参数1，参数2......:运算
# 匿名函数也可以作为一个参数出现
from functools import reduce

s = lambda a, b: a + b
print(s)
print(s(1, 2))

list1 = [3, 5, 8, 9, 0]
m = max(list1)
print('最大值：', m)

list2 = [{'a': 10, 'b': 20}, {'a': 11, 'b': 21}, {'a': 12, 'b': 22}, {'a': 21, 'b': 2}]

m1 = max(list2, key=lambda x: x['a'])

print(m1)

# map 函数

result = map(lambda x: x + 2, list1)
print(list(result))

result1 = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result1))

# reduce(): 对列表中的元素进行加减乘除运算的函数

tuple1 = (1, 2, 5, 3, 2, 1)

result2 = reduce(lambda x, y: x + y, tuple1)

print('----------------34--------------',result2)

'''

注意下面方法的实现
'''
def tesr(sequence, function):
    it = iter(sequence)
    value = next(it)  # 检索 迭代器的下一个值
    value1 = next(it)
    for element in it:  # 上一句已经迭代过一次，这个foreach 则从第二个元素开始迭代了
        value = function(value, value1,element)
    return value


result_test = tesr(tuple1, lambda x, y,z: x + y*z)

print(result_test)

print(id(object()))
print(type(object()))

# 过滤器  filter（过滤方法，需要过滤的可迭代元素）
list3 = [12, 43, 54, 21, 65, 876, 54, 32]

result3 = filter(lambda x: x > 100, list3)

for i in result3:
    print(i)

students = [{'name': 'lucy', 'age': 19}, {'name': 'tom', 'age': 20}, {'name': 'jack', 'age': 21},
            {'name': 'atest', 'age': 22}]
result4 = filter(lambda x: x['age'] > 20, students)
print(list(result4))
list5 = sorted(students, key=lambda x: x['age'], reverse=True)
print(list5)

