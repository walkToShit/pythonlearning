# 文件操作
'''
文件上传
保存log

系统函数  open(file,mode,buffering,encoding)

container = stream.read()  读取管道所有的值
result = stream.readable()判断是否可读
lines = stream.readlines() 读取所有内容到列表中
读取的是图片则不能使用默认的方式  要用RB 的方式读取二进制文件
'''

stream = open(r'E:\pythonLearining\file_learn\a.txt')
# container = stream.read()
# print(container)

result = stream.readable() #判断能不能读

while True:
    line = stream.readline()  #每次读行的时候加了一个换行符
    if line:
        print(line)
    else:
       break
stream = open(r'E:\pythonLearining\file_learn\a.txt')
lines = stream.readlines()
print(lines) #  打印的结果发现每个元素后面都有换行符号
for i in lines:
    print(i)
binarystream = open(r'E:\pythonLearining\file_learn\test.jpg','rb')
print(binarystream.read())
'''
streamWrite = open(r'E:\pythonLearining\file_learn\a.txt','w')
mode 是 w 代表写  每次都是清空文件后再开始写  mode 是a 表示接着写

'''
# 写文件
streamWrite = open(r'E:\pythonLearining\file_learn\a.txt','w')
s = '''
你好！
  欢迎来到这里
              作者：你猜猜
'''

streamWrite.write(s)

streamWrite.close()
streamWriteAppend = open(r'E:\pythonLearining\file_learn\a.txt','a')
streamWriteAppend.write("testappend")
streamWriteAppend.close()

'''
文件的复制

with 结合open 使用  可以帮助我们自动释放资源 相当于close
'''

#read = open(r'E:\pythonLearining\file_learn\test.jpg','rb')

with open(r'E:\pythonLearining\file_learn\test.jpg','rb') as read:
    container = read.read()
    with open(r'E:\pythonLearining\file_learn\linzhiyi.jpg','wb') as write:
        write.write(container)

print("复制完成")

