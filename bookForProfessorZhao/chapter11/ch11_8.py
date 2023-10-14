list1 = [False,"",12,0,13,[],{},()]
print("filter函数返回类型:",type(filter(None,list1)))
list2 = [x for x in range(20)];  # 生成一个0-20的列表
list3 = [x for x in range(20,40)];  # 生成一个0-20的列表
print("map函数返回类型:",type(map(lambda x,y: x * y, list2,list3)))