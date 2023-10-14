list = [x for x in range(20)];  # 生成一个0-20的列表
print(list);  # 打印列表
for y in filter(lambda x: x * 2 > 35, list):  # 选取列表元素中*2 大于35的
    print(y, end=',')



