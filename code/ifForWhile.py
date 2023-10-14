'''
  条件语句(判断) if while for
  print 前的缩进表示是同意if 语句内的。若是没有缩进表示并列。
  即缩进表示括号的意思
'''

username ='1'
if username!='':
    print('嘿嘿 我登录了')
print('------')
#username  作为判断的变量 同C 一样  0 ，none， ''认为是同false  其他同true
if username:
    print('嘿嘿 我登录了')
print('------')

num = 0
if num:
    print('当是0的时候不打印')


if num:
    print('当是0的时候不打印')
else:
    print('当是0的时候打印')

print('*'*10,'居然字符串还能进行乘法我是服了')

#随机数
import random
print(random.randint(1,10))


print()
print()
print()

score = 25

if(score>=85):
    print('优秀')
elif(score>=70):
    print('良好')
elif(score>=60):
    print('及格')
else:
    print('不及格')
print()
print()
print()




'''for 循环   for  变量名 in 集合:
                    语句
'''

#存在continue  关键字
print(list(range(0,8,2)))

for i in range(0,8,2):
     if i==2:
        continue
     print('hello'*i)

#pass 当else 写出来了但是还不确定写什么用pass占位来时语法正确

if 10>7:
    print('11111111')
else:
    pass

#存在break 关键字

for i in range(0,8,2):
     if i==4:
        break
     print('hello'*i)

print()
print()
print()


for i in range(3):
    print(i)
else:
    print("相当于循环到队尾时进行操作")


while i<10:
    print(i)
    i +=1

p = None

print (type(p))
print (type(''))
print (type([]))
print (type({}))
print (type(0))
print (type(()))


#嵌套循环 99乘法表

i = 1

while(i<10):
    j = 1
    while(j<=i):
        print("{}*{}={}".format(j,i,i*j),end = ' ')
        j +=1
    print()
    i +=1















    
