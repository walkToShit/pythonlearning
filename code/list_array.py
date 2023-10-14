#数组的声明
names = ['jack','jack1','jack2','jack3','jack4']
compuetrs_brand = []
test_none = None
#地址  （即使是空数组也是会分配地址的）  连none都分配地址啊！！！
print(id(names))
print(id(compuetrs_brand))
print(id(test_none))
#元素的获取和使用：下标,索引  从0开始
print(names[0])
print(names[1])
#获取最后一个元素
print(names[-1])
print(names[len(names)-1]) #此种方法和java的一样

# 这循环连字符串都行
for i in 'hello':
    print(i,end='#')
print()
for i in names:
    print(i,end='#')

print()
#数组的修改
names[1] = '测试修改'
# 循环修改  基本同java 一样
for i in range(len(names)):
    if names[i] == 'jack1':
        names[i] = 'jackChen'
for i in names:
    print(i,end='#')

print()
print()
print()
print()
print()
print()    
print()
#循环删除
#此种写法 有数组  遍历的跨越现象  就像java中 list循环删除的情况
brands = ['苹果','苹果','华为','小米','OPPO','VIVO']

for i in range(-1,-len(brands),-1):
    if brands[i] == '苹果':
        del brands[i]
        print(i)
#修改上述的缺陷  但是还是有由于数组越界导致错误
##brands = ['苹果','苹果','华为','小米','OPPO','VIVO']        
##for i in range(-1,-len(brands),-1): 
##    while( brands[i] == '苹果'):
##        print(brands[i]) 
##        del brands[i]
##        print(brands)    
#所以解决方案只能使用while  
brands = ['苹果','苹果','华为','小米','OPPO','VIVO'] 
l = len(brands)
i= 0
while i<l:
    while brands[i]=='苹果':   #方式一 此处是用while 循环来解决这个问题
        del brands[i]
        l -=1
    i +=1
print(brands) 

#方式二所以解决方案只能使用 也是外面是while

brands = ['苹果','苹果','华为','小米','OPPO','VIVO'] 
l = len(brands)
i= 0
while i<l:
    if brands[i]=='苹果':   #方式二 用continue来解决问题
        del brands[i]
        l -=1
        continue
    i +=1
print(brands)

print()
print()
print()
print()
print()
print()    
print()
#python  中list 中可以放多种类型数据
testList = ['数字',1,[['1','2']]]
print(testList)

#列表的添加  append() 末尾追加   extend()列表的合并

girls = [];
girls.append('大幂幂')
girls.append('孙尚香')
print(girls)

testList.extend(girls)
print(testList)
# + 也可以用于列表合并
print(testList+girls)
# insert() 指定位置插入
testList.insert(2,'测试插入')
print(testList)
print(testList[::-1])

testList.reverse()
print(testList)

print([1,2,3]*3)














