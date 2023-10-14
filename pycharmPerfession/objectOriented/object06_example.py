# 猫
class Cat:
    type = '猫'

    def __init__(self, nikename, age, color):
        self.nikename = nikename
        self.age = age
        self.color = color

    def eat(self, food):
        print('{}喜欢吃{}'.format(self.type, food))

    def catch_mouse(self, color, weight):
        print('{},抓了一直{}kg的，{}的大老鼠！'.format(self.nikename, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('继续睡觉')
        else:
            print('去抓老鼠')

    def show(self):
        print('猫的详细信息---》',self.nikename, self.age, self.color)


cat1 = Cat('花花', 2, '灰色')
cat1.catch_mouse('黑丝', 2)
cat1.sleep(8)
cat1.eat('小金鱼')
cat1.show()
