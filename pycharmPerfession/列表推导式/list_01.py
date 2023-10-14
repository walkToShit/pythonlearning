# 列表推导式  字典推导式  集合推导式

# 旧的列表---》新的列表

# 列表推导式：格式[表达式 for 变量 in 旧列表]
# 或者 [表达式 for 变量 in 旧列表 if 条件]

names = ['tom', 'lily', 'abc', 'jack', 'java', 'python', 'c']
result = [name for name in names if len(name) > 3]
print(names)
print(result)

result1 = filter(lambda x: len(x) > 3, names)
print(list(result1))

result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 将1-100 能被3整除的组成新的列表

print([i for i in range(1, 101) if i % 3 == 0])

# 0-5 偶数 0-10奇数
# [(偶数，奇数),(0,1),(0,3)....]
newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]-->[3,6,9,5]
listpratice = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
newlist1 = [i[-1] for i in listpratice]
print(newlist1)

dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}

# if 薪资大于5000加200，低于5000加500

listdict = [dict1, dict2, dict3, dict4]
# 下面这句话的if else 是python 的三元表达式
newlistdict = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in
               listdict]
print(newlistdict)

# 修改原字典
for employee in listdict:
    if employee['salary'] > 5000:
        employee['salary'] = employee['salary'] + 200
    else:
        employee['salary'] = employee['salary'] + 500

print(listdict)

# 集合推导式  其实就是列表推导式的去重复版本

listset = [1, 2, 3, 4, 6, 7, 5, 4, 3, 5, 65, 78, 9, 0, 4, 32, 21]

set1 = {i for i in listset}
print(listset)
print(set1)

# 字典的推导式：
dict5 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}

newdict5 = {value:key for key,value in dict5.items()}
print(newdict5)
