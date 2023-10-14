import cv2  #opencv读取的格式是BGR
import matplotlib.pyplot as plt
import numpy as np

plt.show ()
y = [0.0, 0.0, 0.04833333333333333, 0.15583333333333332, 0.35333333333333333, 0.5591666666666667, 0.7141666666666666, 0.7716666666666666, 0.6833333333333333, 0.5141666666666667, 0.35583333333333333, 0.21333333333333335, 0.11583333333333333, 0.0575, 0.0325, 0.019166666666666665, 0.014166666666666666, 0.009166666666666667, 0.005833333333333334, 0.0033333333333333335]
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
plt.plot (x,y)
plt.xlabel ("threshold")
plt.ylabel("accrate")
plt.title('pca')#使用show展示图像
plt.show ()



listAcc = []
print(listAcc.append(1))
print(listAcc)
def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey()
    cv2.destroyAllWindows()
src = r"D:\saveFile\allDevWorkspace\jupyterlab\图像操作\pie2.png"  #带中文的不好用
src_test = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00002.bmp'
#src1 = r"../\jupyterlab\图像操作\pie2.png"
#src = r"C:\Users\lzy25\Desktop\pie2.png"
#img = cv2.imread(src,cv2.IMREAD_GRAYSCALE)#带中文的不好用
img = cv2.imdecode(np.fromfile(src, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)   # 可以使用带中文的路径
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
#cv_show(sobelx,'sobelx')


img = cv2.imread(src_test,cv2.IMREAD_GRAYSCALE)
cv_show(img,'img')

