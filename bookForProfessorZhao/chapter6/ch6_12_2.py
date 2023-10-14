L = ["tom","kate","katy","jack"];        #初始化列表
print("删除数据前："+str(L));               #打印列表
print("第一次删除的内容"+str(L.pop(2)));      #带参数删除指定下标元素
print("第一次删除数据后："+str(L));             #打印列表
print("第二次删除的内容"+str(L.pop()));         #不带参数删除末尾元素
print("第二次删除数据后："+str(L));              #打印列表