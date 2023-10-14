def printparameter(key,key1,**animalcategories):  #  普通参数和可变参数混合
    print(animalcategories)
    for categorie in animalcategories:
        print("键 = %s , 值 = %s" % (categorie, animalcategories[categorie]));

dict1 = {"key1":"cat", "key2":"dog", "key3":"tiger", "key4":"lion"};
printparameter("eagle","wolf",**dict1);  # 普通参数存在key1, 可变参数依旧传入key1 则报错