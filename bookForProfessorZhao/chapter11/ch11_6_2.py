list1 = [False,"",12,0,13,[],{},()]
for y in filter(None,list1):  # 选取列表元素中*2 大于35的
    print(y, end=',')
