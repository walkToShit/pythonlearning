'''

循环导入：  大型python项目中，由于架构不当，可能会出现模块之间的相互导入
  A模块
    def test():
        f()
  B模块
   def f():
        test()

避免产生循环导入：
  1.重新架构
  2.将导入语句放入函数
  3.把导入语句放到模块最后

'''




def task1():
    print('-----task1---' * 5)


def task2():
    print('-----task2---' * 5)
    from module04_importcircle2 import func
    func()


task1()
task2()
'''
ImportError: cannot import name 'func' from 
partially initialized module 'module04_importcircle2' 
(most likely due to a circular import) 循环导入的错误
'''
