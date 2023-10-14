import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import cv2
import os
import math

#file_root = 'D:/Cut_Video/video_data/'  # 当前文件夹下的所有图片
file_root = r'D:/saveFile/videodataSet/source/'  # 当前文件夹下的所有图片

file_list = os.listdir(file_root)

save_out = r'D:/saveFile/videodataSet/dst/'  # 保存图片的文件夹名称

pic_path = 0

for index,video_name in enumerate(file_list):
    video_path = file_root + video_name
    cap = cv2.VideoCapture(video_path)
    # cap = cv2.VideoCapture("1")
    # 创建文件用来保存视频帧
    out_name = os.makedirs(save_out + str(pic_path))

    # 截图的图片命名
    imgPath = ""

    # 视频帧总数
    sumFrame = cap.get(7) #cv2.CAP_PROP_FRAME_COUNT

    #print(sum)
    # 浮点型转整型，计算截取的帧数间隔，这里将截取60张图片 如有修改 切记下列逻辑运算符也一并修改
    time = int(sumFrame / sumFrame)

    # 重置视频总帧数
    sumFrame = 0
    # 需要截取的图片数量
    i = 0

    while True:
        ret, frame = cap.read()
        # 读取视频帧
        if ret == False:
            # 判断是否读取成功
            break
        sumFrame += 1
        if sumFrame % time == 0 and i < sumFrame:
            i += 1
            # 使用i为图片命名
            #out_name = img_name.split('.')[0]
            save_path = save_out + str(pic_path)
            imgPath = save_path + "/%s.jpg" % (str(index)+"_"+str(i))
            # 将提取的视频帧存储进imgPath
            cv2.imwrite(imgPath, frame)
    print("分帧成功%s" % str(pic_path))
    pic_path += 1

    #print("分帧成功")  # 提取结束，打印分帧成功