# 模块os
'''
os.path
os.path.dirname(__file__) 表示当前文件的目录
os.path.join(path,'linzhiyi1.jpg')  拼接路径用的
open(path+r'\linzhiyi.jpg','wb') 我用的字符串拼接也是可以的

container = read.read()
    print(read.name) 获取读取文件的路径名字

'''
import os

print(os.path)
#获取当前文件的绝对路径
path = os.path.dirname(__file__)

print(path)
print(type(path))
path1 = os.path.join(path, 'linzhiyi1.jpg')

print(path1)
print(type(path1))

with open(r'E:\pythonLearining\file_learn\test.jpg', 'rb') as read:
    container = read.read()
    print(read.name)
    with open(path + r'\linzhiyi.jpg', 'wb') as write:
        write.write(container)
    with open('../image' + r'\linzhiyi1.jpg', 'wb') as write:
        write.write(container)

print("复制完成")


r= os.path.isabs(r"E:\pythonLearining\pycharmPerfession\image\linzhiyi1.jpg")

print('----------->>',r)

r1 = os.path.isabs('../image/linzhiyi1.jpg') #../表示返回当前文件的上一级
print(r1)

# 通过相对路径获得绝对路径
#E:\pythonLearining\pycharmPerfession\learnFunction\_init_.py
pathabs = os.path.abspath("_init_.py")
print(pathabs)
#获取当前文件的工作目录
path1  = os.getcwd()
print(path1)
#或最后一个切割名字
result = os.path.split(pathabs)
print(result)
#获取人家你的扩展名  如果给的是目录则元组第二个元素是空
result = os.path.splitext(pathabs)
print(result)
#获取文件大小
size = os.path.getsize("../image/linzhiyi.jpg")
print(size)

# os中的函数  返回指定目录下的所有文件和文件夹
'''
os模块下的方法
os.getcwd() 获取当前目录
os.listdir()浏览目录和文件
os.mkdir() 创建文件夹
os.rmdir()删除空的文件夹
os.remove()删除文件
os.chdir()切换目录
'''
all = os.listdir('../../')
print(all)
testpackage = r'../images'
print(os.path.exists(testpackage))
if not os.path.isdir(testpackage):
    os.mkdir(testpackage)
#如果找不到文件会报错 FileNotFoundError: [WinError 2] 系统找不到指定的文件。: '../image/linzhiyi.jpg'
os.remove('../image/linzhiyi1.jpg')
#os.rmdir('../image')  #OSError: [WinError 145] 目录不是空的。: '../image'
os.removedirs('../images/dsada') # 这方式会一直删除，从右边向左边删除 直至不能删除为止  里面是调用rmdir方法的


os.makedirs()
