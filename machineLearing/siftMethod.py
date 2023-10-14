import numpy as np
import cv2
import matplotlib.pyplot as plt

# 加载图片
img1 = cv2.imread(r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00001.bmp',0)
# img3是和img1一样的照片
img3 = cv2.imread(r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00002.bmp',0)
print(img1.shape,img3.shape)
# 对这张照片进行高斯模糊
blurred = cv2.GaussianBlur(img3, (9, 9), 0)
# 再旋转
(height, width) = blurred.shape[:2]
center = (width//2, height//2)
# 定义旋转矩阵，3个参数分别为：旋转中心，旋转角度，缩放比率
M = cv2.getRotationMatrix2D(center, 90, 1.0)
# 正式旋转，这样就得到了和原始图片img1不太一样的照片
rotated = cv2.warpAffine(blurred, M, (width,height))
img2 = rotated
cv2.imshow("original image",img1)
cv2.waitKey(0)
cv2.imshow("after blurred and rotated",img2)
cv2.waitKey(0)
# 初始化SIFT算子，如果不能用，使用pip安装如下版本的库并重启conda
# pip install opencv-python == 3.4.2.16
# pip install opencv-contrib-python == 3.4.2.16
#sift = cv2.xfeatures2d.SIFT_create()
print("img3",img3)
sift = cv2.SIFT_create()
# 使用SIFT算子计算特征点和特征点周围的特征向量
kp1, des1 = sift.detectAndCompute(img1,None);
kp2, des2 = sift.detectAndCompute(img2,None) #img2
print(kp1,des1,'sdasdsadsadas',kp2,des2)
# BFMatcher中设置knn的k值
bf = cv2.BFMatcher()  #构建特征匹配器
matches = bf.knnMatch(des1,des2, k=2)
print("matches:",matches)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.9*n.distance:# 体现特征点的唯一性
        good.append([m])
print("good",good)
# cv.drawMatchesKnn expects list of lists as matches.
imgNew = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
# 保存图片
cv2.imwrite(r"D:\saveFile\allDevWorkspace\pythonLearining\test\a\imgNew.jpg",imgNew)
# 使用plt绘制
plt.imshow(imgNew),plt.show()

cv2.destroyAllWindows()
