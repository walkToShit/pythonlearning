import cv2
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


# from skimage import filters
# Gabor Filter
def Gabor_filter(K_size=111, Sigma=10, Gamma=1.2, Lambda=10, Psi=0, angle=0):
    # get half size
    d = K_size // 2
    gabor = np.zeros((K_size, K_size), dtype=np.float32)
    # each value
    for y in range(K_size):
        for x in range(K_size):
            # distance from center
            px = x - d
            py = y - d
            # degree -> radian
            theta = angle / 180. * np.pi
            # get kernel x
            _x = np.cos(theta) * px + np.sin(theta) * py
            # get kernel y
            _y = -np.sin(theta) * px + np.cos(theta) * py
            # fill kernel
            gabor[y, x] = np.exp(-(_x ** 2 + Gamma ** 2 * _y ** 2) / (2 * Sigma ** 2)) * np.cos(
                2 * np.pi * _x / Lambda + Psi)
    # kernel normalization
    gabor /= np.sum(np.abs(gabor))
    return gabor


# 使用Gabor滤波器作用于图像上
def Gabor_filtering(gray, K_size=11, Sigma=10, Gamma=1.2, Lambda=10, Psi=0, angle=0):
    # get shape
    H, W = gray.shape
    # padding
    gray = np.pad(gray, (K_size // 2, K_size // 2), 'edge')
    # prepare out image
    out = np.zeros((H, W), dtype=np.float32)
    # get gabor filter
    gabor = Gabor_filter(K_size=K_size, Sigma=Sigma, Gamma=Gamma, Lambda=Lambda, Psi=0, angle=angle)
    # filtering
    for y in range(H):
        for x in range(W):
            out[y, x] = np.sum(gray[y: y + K_size, x: x + K_size] * gabor)
    out = np.clip(out, 0, 255)
    out = out.astype(np.uint8)
    return out


# 使用6个不同角度的Gabor滤波器对图像进行特征提取
def Gabor_process(img):
    # get shape
    H, W = img.shape
    outs = []
    # define angle
    # As = [0, 45, 90, 135]
    As = [0, 30, 60, 90, 120, 150]
    out = np.zeros([H, W], dtype=np.float32)
    # each angle
    for i, A in enumerate(As):
        # filtering image
        out = Gabor_filtering(img, K_size=30, Sigma=5, Gamma=1.2, Lambda=5, angle=A)
        # gabor_filter
        # out = Gabor_filter(K_size=30, Sigma=5, Gamma=1.2, Lambda=5, angle=A)
        # out=cv2.getGaborKernel((30,30),sigma=5,theta=np.pi*A/180,lambd=5,gamma=1.2,ktype=cv2.CV_32F)
        # out=filters.gabor_kernel(frequency=0.1,theta=np.pi/2,n_stds=3)
        out = np.array(out)
        pl.subplot(1, 6, i + 1)  # 画1*6格子
        pl.imshow(out, cmap='gray')
        outs.append(out)
    pl.show()
    return outs


if __name__ == '__main__':
    # Read image
    img_src = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00002.bmp'
    image = cv2.imread(img_src).astype(np.float32)
    img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # gabor process
    out = Gabor_process(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
