def printparameter(**animalcategories):  # 打包为字典
    print(animalcategories)
    for categorie in animalcategories:
        print("键 = %s , 值 = %s" % (categorie, animalcategories[categorie]));

dict1 = {"key1":"cat", "key2":"dog", "key3":"tiger", "key4":"lion"};
print("打印字典",end = '');
print(dict1);
printparameter(**dict1);        #字典需要拆包后传入