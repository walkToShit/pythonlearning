'''

面相对性：
程序  现实中
对象 ---》 具体的事物


好处：

'''


# 定义类和属性
# 所有类名要求首字母大写，多个单词使用驼峰式命名

class PhoneTest:
    # 类属性
    brand = 'test'


print(PhoneTest)
# 创建对象方式
objecta = PhoneTest()
print(objecta)
print(objecta.brand)
objectb = PhoneTest()
objectb.brand = 'huawei'
print(objectb)
print(objectb.brand)
#删除类属性在对象中的值后还可获取类属性的初始值  我也是服了
del objectb.brand
print(objectb.brand)

class Student:
    name = ''
    age = ''
