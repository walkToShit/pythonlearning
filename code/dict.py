#字典  键值对的方式
#声明方式 {}  有点 restful 风格的方式   与java中的Map 相似  
dict1 = {} # 空字典
dict2 = dict() #  list = list() 空列表   tuple = tuple() 空元组
dict3 = {'id':'210106199002054015','sex':'0'}
print(dict3)
#元组转字典
dict4 = dict((('id','210106199002054015'),('sex','0')))
#或者用列表也可以 dict([('id','210106199002054015'),('sex','0')])
print(dict4)
#字典的增删改查
dict6 = {}
#增加 格式 ： dict[key] = value  key可以是多种类型
# 当key相同时 则是修改
dict6['name'] = 'linzhiyi'
print(dict6)
dict6['name'] = 'nicai'
print(dict6)
dict6[1] = 'linzhiyi'
dict6[('1','2')] = 'linzhiyi'
print(dict6)
#字典的循环遍历 key
for key  in dict6:
    print(key, end ='#' )
print()
#字典的内建函数  items() values()  keys()
print(dict6.items())
print(dict6.values())
print(dict6.keys())

#查询 dict[‘key’] 查询不到会报错  可以用内建方法get
# dict.get('key',default) 查询不到 则赋值默认值
print(dict6.get('2',1234))
#删除
##del dict6['3'] #爆出没有对应key 的错误
result = dict6.pop(1,100)
print(result)
print(dict6)


print()
print()
print()
print()


#字典的合并  相同的覆盖  不同的补充
dict7 = {1:2,2:3}
dict8 = {1:21,3:3}
dict7.update(dict8)
dict7.update((('id','210106199002054015'),('sex','0')))
print(dict7)

#转换为字典的类方法
print()
print()
print()
print()
dict10 = dict.fromkeys([1,2,3,4],10)
print(dict10)






















