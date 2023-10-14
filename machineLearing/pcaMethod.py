# encoding:GBK
'''
����PCA��ͼ��ά���ع�
'''
import numpy as np
import cv2 as cv


# �������Ļ�
def Z_centered(dataMat):
    rows, cols = dataMat.shape
    meanVal = np.mean(dataMat, axis=0)  # �������ֵ��������������ľ�ֵ
    meanVal = np.tile(meanVal, (rows, 1))  # ��X�Ḵ��1������Y�Ḵ��rows��
    newdata = dataMat - meanVal  # �����
    return newdata, meanVal


# Э�������
def Cov(dataMat):
    rows, cols = dataMat.shape
    meanVal = np.mean(dataMat, 0)  # ѹ���У�����1*cols���󣬶Ը������ֵ
    meanVal = np.tile(meanVal, (rows, 1))  # ����rows�еľ�ֵ����
    Z = dataMat - meanVal
    # Z = dataMat
    Zcov = (1 / (cols - 1)) * Z.T * Z
    return Zcov


# ��С����ά��ɵ���ʧ��ȷ��k
def Percentage2n(eigVals, percentage):
    sortArray = np.sort(eigVals)  # ����
    sortArray = sortArray[-1::-1]  # ��ת��������
    arraySum = sum(sortArray)
    tmpSum = 0
    num = 0
    for i in sortArray:
        tmpSum += i
        num += 1
        if tmpSum >= arraySum * percentage:
            return num


# �õ�����k������ֵ����������
def EigDV(covMat, p):
    D, V = np.linalg.eig(covMat)  # �õ�����ֵ����������
    k = Percentage2n(D, p)  # ȷ��kֵ
    eigenvalue = np.argsort(D)  # ����������ȡ������
    K_eigenValue = eigenvalue[-1:-(k + 1):-1]  # ȡ��k��ֵ��[::-1]
    K_eigenVector = V[:, K_eigenValue]
    return K_eigenValue, K_eigenVector


# �õ���ά�������
def getlowDataMat(DataMat, K_eigenVector):
    return DataMat * K_eigenVector


# �ع�����
def Reconstruction(lowDataMat, K_eigenVector, meanVal):
    reconDataMat = lowDataMat * K_eigenVector.T + meanVal
    # reconDataMat = lowDataMat * K_eigenVector.T
    return reconDataMat


# PCA�㷨
def PCA(data, p):
    dataMat = np.float32(np.mat(data))
    # �������Ļ�
    dataMat, meanVal = Z_centered(dataMat)
    # ����Э�������
    covMat = Cov(dataMat)
    # covMat = np.cov(dataMat, rowvar=0) #0��ʾ��
    # �õ�����k������ֵ����������
    D, V = EigDV(covMat, p)
    # �õ���ά�������
    lowDataMat = getlowDataMat(dataMat, V)
    # �ع�����
    reconDataMat = Reconstruction(lowDataMat, V, meanVal)
    return reconDataMat


def pcaMethod(image):
    #imagePath = r'D:\saveFile\allDevWorkspace\dataSet\palmprint\session2\00002.bmp'
    #image = cv.imread(imagePath)
    #image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    rows, cols = image.shape
    #cv.imshow('original', image)
    reconImage = PCA(image, 0.9)
    reconImage = reconImage.astype(np.uint8)
    #cv.imshow('test', reconImage)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return reconImage.ravel()


