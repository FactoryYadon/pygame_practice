import numpy as np
import cv2
import os

from random import shuffle
import math

def onChange(x):
    pass


def track_bar():
    folder_path = (os.path.dirname(os.path.realpath(__file__)))                         # 실행 스크립트 폴더 절대 경로
    image_folder_path = os.path.join(folder_path,"images")                              # images 폴더 경로

    img_file = os.path.join(image_folder_path,"test_img.png")                                # img_file 경로
    
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)                                         # IMREAD_COLOR 칼라이미지 생성
    cv2.imshow('original',img)

    subimg = img[300:400, 350:750]
    cv2.imshow("cutting",subimg)

    img[300:400 , 0:400] = subimg


    print(img.shape)
    print(subimg.shape)

    cv2.imshow('modified',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


track_bar()