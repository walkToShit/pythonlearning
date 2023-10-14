#运算符


name = 'admin'

name1 = name

print(id(name),name)
print(id(name1),name1)

name2 = name
print(id(name2),name2)


#id  This is the address of the object in memory.

print(name==name1)
num =8
num += 5
print(num)

a='abc'
a +='ff'
print(a)

a = 8
b = 2

#  ** 表示 指数
result = a**b
print(result)

#   // 表示取整  向下取整
print(a//b)
a=9
print(a//b)
#   % 取余
print(a%b)



m1 = input('第一个数字')
m2 = input('第二个数字')


print(m1==m2)


m1 = 'hello'
m2 = 'hello'
print(m1==m2)



money =2000000
salary = 2000000

print(id(money))
print(id(salary))

print (money is salary)

print (money is not salary)



print()
print()
print()
print()
print()
print()


#十进制转化为二进制     二进制转化为十进制   0b（零b）表示二进制  0o(零O)表示八进制
print(bin(123))
print(int(0b1101))
print(int(0o1101))

print(bin(-8))


print()
print()
print()
print()
print()
print()



# 按位与& 或| 异或^(相同的为0不同为1)    非~

a= 1
b = 2

print(a&b)
print(a|b)
print(a^b)
print(~a)

print()
print()
print()
#位移运算符
print(a<<1)
print(8>>1)


print(35>>4)
print(128<<1)



print()
print()
print()
#python 中支持复数的运算
print(complex(0,1)*complex(0,1))

#三元运算符

#result = (8>10) ? 'f':'t'  这种格式python 不支持
#python  格式   结果1 if (判断式) else  结果2    即：判断式为真 结果一 为假结果2

result = 10 if 10>8 else 8

print(result)



















































































