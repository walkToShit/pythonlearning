'''
公路（road）:
           属性：公路名称，公路长度
车（Car）:
          属性：车名，时速
          方法： 1.求车名在那条公路上以多少的时速行驶了多长
                  get_time(self,road)
                2.初始化车属性信息__init__方法
                3.打印对象现实车的属性

'''
import random


class Road:
    def __init__(self, name, length):
        self.name = name
        self.length = length

class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def get_time(self,road):
        random_time = random.randint(1,10)
        msg = '{}品牌的车在{}以上{}速度行驶{}小时'.format(self.brand,road.name,self.speed,random_time)
        print(msg)

road =Road('京藏告诉',12000)
audi = Car('奥迪',120)
audi.get_time(road)
