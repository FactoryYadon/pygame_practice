import cv2
import numpy as np
import os

def showimage():
    folder_path = (os.path.dirname(os.path.realpath(__file__)))                         # 실행 스크립트 폴더 절대 경로
    image_folder_path = os.path.join(folder_path,"images")                              # images 폴더 경로

    img_file = os.path.join(image_folder_path,"background.png")                         # img_file 경로
    img_file = img_file.replace("\\","/")
    # print(img_file)
    
    img_array = np.fromfile(img_file, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)                                     # IMREAD_COLOR 칼라이미지 생성

    
    

    cv2.imshow("model",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


showimage()


