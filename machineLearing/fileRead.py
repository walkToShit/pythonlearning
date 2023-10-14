import os
import numpy as np
import cv2
from datetime import datetime as dt
from pcaMethod import pcaMethod
#from os.path import join, getsize

listPicrtueAll = np.array([]); #用于存储所有图片的
listPicrtueClasscify = np.array([]); #用于存储分类均值数据的
listPicrtueTemp = np.array([]); #用于存储临时数据的

print(os.getcwd()) # 获取当前路径
path = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2' #\00002.bmp
s1 = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\{}'
imagepath = s1.format("00002.bmp")
# 记录图像的大小
x,y = cv2.imread(imagepath, cv2.IMREAD_GRAYSCALE).shape
sumtest = 1200; #总共需要比对的数据
sumScore= 0; #的分数
threshold = np.array(range(20))
print(threshold)
listAcc = [] # 记录不同阈值的准确率
#读取灰度图片，
def readimage(path):
    img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img1;



for root, dirs, files in os.walk(path):
    picrures = files;
print(picrures,len(picrures))
print(len(picrures))

peopleList = list();  #用于存储所有图片信息所属类别
for num in range(len(picrures)):
    peopleList.append(int(np.floor(num/10)));
print(peopleList)

print("开始：进行特征提取",dt.now())
for i,name in enumerate(picrures):   #i  0~5999
   # if i >=20:
      #  break
    img = pcaMethod(readimage(s1.format(name))) # 拼接地址读取图像
    if i == 0:
        listPicrtueAll = np.array(img,ndmin = 2)
    else:
        listPicrtueAll=np.append(listPicrtueAll,np.array(img,ndmin = 2),axis = 0)
    if i%10 ==0:
        listPicrtueTemp = np.array(img,ndmin = 2) #临时数组初始化
    if (i % 10 == 8)&(i<10):
        listPicrtueClasscify = np.array(listPicrtueTemp.mean(axis = 0),ndmin = 2) #分类数组初始化
        listPicrtueTemp = np.array([])  # 清空临时数组为下一组求均值做准备
        continue
    if (i % 10 == 8) & (i > 10):
        listPicrtueClasscify = np.append(listPicrtueClasscify,np.array(listPicrtueTemp.mean(axis = 0),ndmin = 2),axis = 0)
        listPicrtueTemp = np.array([]) # 清空临时数组为下一组求均值做准备
        continue
    if i % 10 == 9:
        continue
    if i % 10 != 0:
        print(i)
        print(img.shape)
        listPicrtueTemp=np.append(listPicrtueTemp,np.array(img,ndmin = 2),axis = 0)

print("结束：",dt.now())

for thresholds in threshold:
    listPicrtueAll = np.c_[listPicrtueAll,np.array(peopleList)] # 拼接数据
    for i, test in enumerate(listPicrtueAll):
        if(i%10==8)|(i%10==9):
            for spe,classify in enumerate(listPicrtueClasscify):
                print(spe,np.std((classify - test[0:x * y])),test[x * y])
                if (np.std((classify - test[0:x * y])) < thresholds):
                    if test[x * y] == spe:
                        sumScore += 1
                    break;
    listAcc.append(sumScore / sumtest)
    sumScore = 0; # 更换阈值后 对得分初始化

print("判分结束，准确率为：",listAcc)




