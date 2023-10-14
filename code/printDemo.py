#print 用法
name ="小林"
age='30'
gender='男'

#默认的间隔符为空格   可通过sep 设置为其他字符
print(name,age,gender)

print(name,age,gender,sep='#')

#print 默认结束换行
print("----------结束end 关键字----------")
print(name)
print(age)
print(gender)
print(name,end="_")
print(age,end="_")
print(gender,end="_")

print("hello\nworld")  
print(name,'\n',age,'\n',gender,'\n')


#转义字符

print('hello\p\tyton')
print('hello\p\\tyton')

#原样输出 r   raw 的意思
print(r'hello\p\tyton')

# ''  ""  ''' '''   单引号 双引号标识字符串  三引号标识原样式输出
print('淘宝，你正在使用验证码登陆，验证码是：1234，涉及个人账户安全请保密！')

print('淘宝，你正在使用验证码登陆，\n验证码是：1234，\n涉及个人账户安全请保密！')

print('''淘宝，
你正在使用验证码登陆，
验证码是：1234，
涉及个人账户安全请保密！''')

#格式化输出
person='小林'
address = '沈阳市铁西区'
phone = '1234567890'
num = 2
# 由于在python 中 字符串+ 不被视为连接操作 ，而是视为加法操作 导致报错  与java 中不同
# print('订单的收件人是:'+person,'收货地址是:'+address,'联系方式:'+phone,'数量'+num)
print('订单的收件人是:%s,收货地址是:%s,联系方式:%s,数量:%s' % (person,address,phone,num))
# %d 只取得整数部分
age=18.6
print('年龄是:%d'% age)
# %f 单精度浮点 .1表示四舍五入取1位小数   .2 表示四舍五入取两位
salary = 15622.21  
print('工资是:%.1f'% salary)


movie='小电影'
price = 45.6
num = 40

message = '''
电影名称:%s
票价:%.1f
数量:%d
总价:%.1f)'''
print(message %(movie,price,num,num*price))

total = num*price
message = '''
电影名称:%s
票价:%.1f
数量:%d
总价:%.1f'''%(movie,price,num,total)
print(message)
print('\n\n\n\n\n\n\n\n\n')




#字符串的format 方法
age =2
s='已经上'
message='乔治说：我今年{}岁了，{}幼儿园'.format(age,s)
print(message)

