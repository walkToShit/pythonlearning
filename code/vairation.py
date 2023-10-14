money=99
count=5
person = '小林'

print(money,type(money))
print(count,type(count))
print(person,type(person))



money = 9.9
print(money,type(money))


money = '9.9元'
print(money,type(money))

# 下面的赋值行为证明了python 为强类型语言  java 中字符串是 连接操作不视为加法
money = 9.9+'元（粘结字符串）'
print(money,type(money)) 
