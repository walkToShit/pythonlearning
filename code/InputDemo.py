#输入 input()

name = input("您的名字是：")

age = input("您的年龄是:")

print(type(age))


#print('尊敬的{}:您好 您的年龄为{}，有些偏大)')
print('''尊敬的{}:您好
              您的年龄为{}，有些偏大)'''.format(name,age))

