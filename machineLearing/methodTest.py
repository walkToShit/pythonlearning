import numpy as np
import pandas as pd
import cv2
from pcaMethod import pcaMethod
#读取灰度图片，
def readimage(path):
    img1 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img1;
path = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2' #\00002.bmp
imagepath = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00002.bmp'
imagepath1 = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00011.bmp'
image = cv2.imread(imagepath,0)
listPicrtue = np.array([]);
# 加载图片
img1 = cv2.imread(r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00001.bmp',0)
image_ravel =image.ravel()
print(image_ravel.ndim,image_ravel,image_ravel.shape)
listPicrtue = np.array(image_ravel,ndmin = 2)
print("image",image.shape,"img1",img1.shape)
print("listPicrtue",listPicrtue)
print("-----------------------------------------------------------")
listPicrtue =np.append(listPicrtue,np.array(img1.ravel(),ndmin = 2),axis = 0)
listPicrtue =np.append(listPicrtue,np.array(img1.ravel(),ndmin = 2),axis = 0)
listPicrtue =np.append(listPicrtue,np.array(img1.ravel(),ndmin = 2),axis = 0)
listPicrtue =np.append(listPicrtue,np.array(img1.ravel(),ndmin = 2),axis = 0)
print(listPicrtue)
pdd = pd.DataFrame(listPicrtue)
print(pdd.iloc[0])

print("计算平均值",listPicrtue.mean(axis = 0)) #np.mean(listPicrtue,0)

x_train = pcaMethod(readimage(imagepath))
x_test = pcaMethod(readimage(imagepath1))
print(np.std((x_test - x_train)))
#print(np.sqrt(sum((x_test - x_train) ** 2)))










