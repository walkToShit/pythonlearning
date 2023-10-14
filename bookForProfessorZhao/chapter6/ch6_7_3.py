L = [1,2,3];    # 初始化一个列表
L1 = [3,4,5,6]; # 初始化一个列表
LRecp = [x for m in (L,L1) for x in m]  # 使用推导式进行合并
print(LRecp);