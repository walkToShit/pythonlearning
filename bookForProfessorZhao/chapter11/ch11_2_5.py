def printparameter(*animalcategories): #打包为元组
    print(animalcategories)
    for categories in animalcategories:
        print(categories);


printparameter("cat","dog","tiger","lion");