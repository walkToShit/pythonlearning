


'''is 比较的是两个对象的id值是否相等，
也就是比较俩对象是否为同一个实例对象，是否指向同一个内存地址。

==
比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。
'''
str = 'abc'
str1= "abc"
str2 = '''abc
'''
print(id(str),id(str1),id(str2))

print(str == str1)
print(str is str1)

print(str1 == str2)
print(str1 is str2)


# input 对字符串进行了操作 导致生成不同的对象
#相当于  java 中 new String("bala..")
'''s1 = input("请输入s1")
s2 = input("请输入s2")

print(id(s1),id(s2))
print(s1 == s2) #true
print(s1 is s2) #地址不同
'''


str4 = str + str1  # 字符串连接
str5 = str1*5      #字符串乘法

print(str4,str5,sep='#')


name ='steven'

result = 't' in name
#判断字符串是否有包含另一个字符串
print(result)


result = 'tv' not in name
print(result)


print('%s说:\'哈哈哈\''%name)

#r 字符串格式原样输出
print(r'%s说:\'哈哈哈\''%name)
print('''%s说:\'哈哈哈\''''%name)

print()
print()
print()
name ='steven'
print(name[2])
print(name[0:3])#从零开始  包前不包后
print(name[3:])#从某一位开始 直至结尾
print(name[:4])#从0位开始 直至某一位
print(name[:-1])# 负数表述从后向前数
#[值1:值2:值3]   值1位开始位置  值2位置终止位置（包前不包后）
#值3  -1表示逆向（以1位间隔取值）  1表示正向取值 （以1为间隔）
#值3  可以为其他数值 +-表示方向   数字表示间隔数字
# 若是不填数字默认 正向从头到尾  逆向 从尾到头
print(name[::-1])
print('--->',name[5:0:-3])
print('--->',name[::2])

print()
print()
print()


# 字符串相关的 查找 替换
# find() rfind()  index()  rindex() replace()

s1 = 'index lucy lucky goods'
result =  'R' in s1
print(result)
position = s1.find('R') # 返回值-1 代表没有找到
print(position)
position = s1.find('l') #如果可以找到则反悔字符第一次出现的位置
print(position)
position=s1.find('l',position+1,len(s1)-5)#也可以制定开始和截止位置
print(position)
url = 'http://www.voidcn.com/article/p-tolaheto-bue.html'
position = url.rfind('/') # 从右侧开始找
print(position)
#index() 同 find 一样只不过没找到就报错
print(s1.replace(' ','#',1))   #replace(old, new[, count])  第三个参数可不写

print()
print()
print()

msg = '上课了！认真听课！'
#编码之后的结果
result = msg.encode('utf-8')
print(type(result))   #编码之后是 <class 'bytes'>注意
print(result)
#解码之后的结果  decode 不是str 的方法注意
result = result.decode('utf-8')
print(result)
#startswith()  endswith()  判断以什么为开始   以什么为结束
url = 'http://www.voidcn.com/article/p-tolaheto-bue.html'
result = url.startswith('http')
print(result)
result = url.endswith('html')
print(result)
#isalpha() 是否是字母  isdigit()是否是数字
testString = 'abcd'
result = testString.isalpha()
print(result)
result = testString.isdigit()
print(result)

print()
print()
print()

#join(seq) 方法  将'-'加入到字符串并将每个速用'-'连接

new_str = '-'.join('abc')
print(new_str)

list1 =['a','b','c','d']
new_str = '-'.join(list1)
print(new_str)


print()
print()
print()
#strip()  split()返回一个list 

str1 = "   hello world  "

print(str1.lstrip()+'test')
print(str1.rstrip()+'test')
print(str1.strip()+'test')

#split 分割同java中有点不同
str1 = str1.split(' ')

print(str1)
#count() 
print("   hello world  ".count('l'))









