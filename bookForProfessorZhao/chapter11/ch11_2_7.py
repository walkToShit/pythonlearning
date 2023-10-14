def printparameter(**animalcategories):  # 打包为字典
    print(animalcategories)
    for categorie in animalcategories:
        print("键 = %s , 值 = %s" % (categorie, animalcategories[categorie]));


printparameter(key1="cat", key2="dog", key3="tiger", key4="lion");  #使用关键字方式传递参数