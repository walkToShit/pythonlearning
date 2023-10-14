def describstudent(name, sex="不明确"):
    '''用于描述学生的函数'''
    print("学生的名字是：%s   学生的性别是：%s" % (name, sex));


describstudent("Tom");        #当实参没有为sex赋值，则会调用sex参数的默认值
