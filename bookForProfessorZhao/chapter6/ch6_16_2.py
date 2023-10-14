L = ["tom","kate","katy","Aaron","katy","jack"];        #初始化列表
L1 = L;                                                  #复制列表
L.append("test1");                                      #添加元素到原列表
L1.append("test2");                                      #添加元素到复制列表
print("打印原列表："+str(L));
print("打印复制后的列表："+str(L1));