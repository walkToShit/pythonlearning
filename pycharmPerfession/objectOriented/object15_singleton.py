# 单例模式
# 开发

class Singleton:
    __instance = None
    name = 'li'
    def __init__(self):
        self.name ='xi'
    # 重写 __new__()
    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


test = None

print(test == None)
print(test is None)

s = Singleton()
s1 = Singleton()
print(dir(s1))
print(s, s1)
print(s.name)
print(s.__class__)
print(s.__class__.name)
del s.name
print(s.name)
