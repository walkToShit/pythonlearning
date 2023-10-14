'''is 比较的是两个对象的id值是否相等，
也就是比较俩对象是否为同一个实例对象，是否指向同一个内存地址。

==
比较的是两个对象的内容是否相等，默认会调用对象的__eq__()方法。
'''
str0 = 'abc'
str1= "abc"
str2 = '''abc'''
print(list(str0));   #打印字符串
print(list(str2));   #打印字符串
print(id(str),id(str1),id(str2))  #查看不同形式声明字符串的地址
print(str0 == str1)
print(str0 is str1)
print(str1 == str2)
print(str1 is str2)
print(str1 is not str2)


