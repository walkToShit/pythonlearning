# 私有化
'''
好处：
   1.隐藏属性不被外界随意修改
   2.也可以修改：通过函数
     def serXXX(self,xxx):
     可以对参数加以限制
   3.如果想获得一个具体属性 用get方法

'''
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score = 59
    def __str__(self):
        return '姓名：{}，年龄：{}，考试分数:{}'.format(self.name,self.age,self.__score)
    def getscore(self):
        return self.__score
    def setscore(self,score):
        if score>0 and score<100:
            self.__score = score
        else:
            print("分数不在正确范围内")

student = Student('jack',18);
#print(student.__score) #没赋值之前  AttributeError: 'Student' object has no attribute '__score'
student.__score = 95 # 这也不报错
print(student)
print('我是新设置的属性__score',student.__score) # 在赋值之后 也能输出了（这也是很迷惑啊）
print('我是私有属性:',student.getscore())
#看一个对象里面的所有属性
print(dir(Student))
print(dir(student)) # 系统将私有属性改名了 _Student__score
print(student._Student__score) #私有属性还是能直接获取  真是优秀

print(dir())

print('-------------分割----------'*10)