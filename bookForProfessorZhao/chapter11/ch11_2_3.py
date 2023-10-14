def describStudent(name = "tom",sex):     #若是 参数默认值不在形参列表的右侧则会报错
    '''用于描述学生的函数'''
    print("学生的名字是：%s   学生的性别是：%s" %(name,sex));

describStudent(sex = "女")