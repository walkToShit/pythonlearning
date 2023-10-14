list1 = [x for x in range(20)];  # 生成一个0-20的列表
list2 = [x for x in range(20,40)];  # 生成一个0-20的列表
result = map(lambda x,y: x * y, list1,list2)
print("使用lambda表达式作为func:",list(result))


def func(a,b):
    return a+b;


print("使用普通函数作为func:",list(map(func, list1,list2)))