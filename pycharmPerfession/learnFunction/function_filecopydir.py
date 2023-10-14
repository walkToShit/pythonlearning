# 封装城函数
import os


def copy(src, target):
    if os.path.isdir(src):
        filelist = os.listdir(src)
        for file in filelist:
            olddir = os.path.join(src, file)
            newdir = os.path.join(target, file)
            if  os.path.isdir(olddir):  # 如果 复制来源是个目录
                if not os.path.exists(newdir): # 判断目标是否存在相应文件夹
                    os.makedirs(newdir)        # 不存在则创建文件夹
                    copy(os.path.join(src, file), newdir) #递归调用
            else:
                path = os.path.join(src, file)
                with open(path, 'rb') as rstream:
                    container = rstream.read()
                    path1 = os.path.join(target, file)
                    with open(path1, 'wb')as wstream:
                        wstream.write(container)

copy(r'E:\pythonLearining\test\a', r'E:\pythonLearining\test\b')


