#元组类型 tuple
#空的时候 类型为tuple
t1 = ()
print(type(t1))
#当只有一个元素的时候， 为该元素的类型
t2 = ('hello')
print(type(t2))  # 是str 类型
#当只有一个元素的时候，加,后 为tuple类型
t2 = ('hello',)
print(type(t2))

list1 = ['2','3','4','5','1','1']
#转换为元组
t3= tuple(list1)
print(t3)

#查询 则使用下表和切片的方式  同列表
print(tuple('dsadsa'))
#print(tuple(1121)) TypeError: 'int' object is not iterable 

#查询元组中 元素的个数  和该元素的位置
print(t3.count(7))
try:
 print(t3.index(7))
except:pass
print()
print()
print()
print()
#拆包  当元素不一致时 会报错

t1 =(1,2,3)
a,b,c = t1
print(a,b,c)


# 当变量个数与元组个数不一致  可以有 通配*

t1 = tuple('123456678')
a,*b,c = t1
print(a,b,c)
a,b,*c = t1
print(a,b,c)


a,b,*c =list1
print(a,b,c)
