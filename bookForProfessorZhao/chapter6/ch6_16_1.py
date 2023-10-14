L = ["tom","kate","katy","Aaron","katy","jack"];        #初始化列表
L1 = L.copy();                                        #复制列表
L.append("test");                                     #修改源列表 不影响复制后的列表
print("打印复制后的列表："+str(L1));