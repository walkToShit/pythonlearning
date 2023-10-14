class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score = 59
    def __str__(self):
        return '姓名：{}，年龄：{}，考试分数:{}'.format(self.name,self.age,self.__score)
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        if score > 0 and score < 100:
             self.__score = score
        else:
             print("分数不在正确范围内")
    @score.deleter
    def score(self):
        print('-----删除属性的时候进入+++++++________-----------')
        del self.__score

student = Student('chen',18)
print(student.score)
student.score = 130
print(dir(student))
del student.score  # 属性删除后  私有属性_Student__score 消失了
print(dir(student))
print(student.score)
# print(student.score())