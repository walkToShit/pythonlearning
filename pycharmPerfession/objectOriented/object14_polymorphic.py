class Person:
    def __init__(self,name):
        self.name = name

    def feed_pet(self,pet):
        if isinstance(pet,Pet):
            print('{}喜欢养宠物：{},昵称是{}'.format(self.name,pet.role,pet.nikename))
        else:
            print("不是宠物类型")
            pet.eat()

class Pet:
    role = 'Pet'
    def __init__(self,nikename,age):
        self.nikename =nikename
        self.age =age
    def show(self):
        print('昵称：{}，年龄：{}'.format(self.nikename,self.age))

class Cat(Pet):
    role='mao'
    def catch_mouse(self):
        print('抓老鼠。。。。')

class Dog(Pet):
    role ='gou'
    def watch_house(self):
        print('看家高手。。。。')
class Tiger:
    def eat(self):
        print("太可爱了，能吃人")
cat = Cat('huahua',2)
dog = Dog('大黄',4)
tiger =Tiger()
person = Person('lucy')
person.feed_pet(cat)
person.feed_pet(tiger)
