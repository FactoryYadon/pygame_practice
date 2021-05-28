import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def showimage():
    folder_path = (os.path.dirname(os.path.realpath(__file__)))                         # 실행 스크립트 폴더 절대 경로
    image_folder_path = os.path.join(folder_path,"images")                              # images 폴더 경로

    img_file = os.path.join(image_folder_path,"background.png")                                # img_file 경로
    
    # img = cv2.imread(img_file, cv2.IMREAD_COLOR)                                         # IMREAD_COLOR 칼라이미지 생성
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)                                     # IMREAD_GRAYSCALE 흑백이미지 생성

    plt.imshow(img, cmap="gray" , interpolation="bicubic")
    plt.xticks([])
    plt.yticks([])
    plt.title("model")
    plt.show()    
    
    
    
    
    # cv2.namedWindow("model",cv2.WINDOW_NORMAL)                                          # 원본 이미지 크기로 윈도우 생성 후 사용자가 크기 조절 가능
    # cv2.imshow("model",img)
# 
# 
    # k = cv2.waitKey(0) & 0xFF
# 
    # if k == 27:
        # cv2.destroyAllWindows()
    # elif k == ord('c'):
        # cv2.destroyAllWindows()


showimage()


