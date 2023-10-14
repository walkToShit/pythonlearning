matrix = [[1,2,3],[2,3,4],[4,5,6]]; # 声明一个列表
list1 = [row[1]+1 for row in matrix]; # 选取第二列元素+1 形成新的列表并返回
print(list1);

list1 = [row[1]+1 for row in matrix if row[1]>3]; #选取第二列大于3的元素+1 形成新的列表并返回
print(list1);