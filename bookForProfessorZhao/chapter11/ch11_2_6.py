def printparameter(*animalcategories): #打包为元组
    print(animalcategories)
    for categories in animalcategories:
        print(categories);

list1 = ["cat","dog","tiger","lion"];
tuple1 = tuple(list1);
print("打印列表 ",end = '');
print(list1);
print("打印元组 ",end = '');
print(tuple1);
printparameter(*list1);   #列表拆包后传入
printparameter(*tuple1);  #元组拆包后传入
