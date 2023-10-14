# input 对字符串进行了操作 导致生成不同的对象
#相当于  java 中 new String("bala..")
s1 = input("请输入s1")
s2 = input("请输入s2")

print(id(s1),id(s2))
print(s1 == s2) #true
print(s1 is s2) #地址不同