def printparameter(name,*animalcategories): # 指定参数在可变参数之前
    print( name,"认识的动物种类: " ,end = '')
    for categories in animalcategories:
        print(categories,end=',');

list1 = ["cat","dog","tiger","lion"];
print("打印列表 ",list1);
printparameter("tom",*list1);   #列表拆包后传入

