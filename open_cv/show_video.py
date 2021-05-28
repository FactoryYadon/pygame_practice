import cv2
import numpy as np
import os
import time
# import matplotlib.pyplot as plt

def show_Video():
    try:
        print("카메라를 구동합니다.")
        cap = cv2.VideoCapture(0)
    except:
        print("카메라 구동 실패")
        return

    fps = 20.0
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc("D","I","V","X")

    out =cv2.VideoWriter("mycam.avi",fcc,fps,(width,height))
    print("녹화를 시작합니다.")
    
    # cap.set(3,480)
    # cap.set(4,320)


    while True:
        ret , frame = cap.read()

        if not ret:
            print("비디오 읽기 오류")
            break

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("video",gray)

        out.write(gray)

        k = cv2.waitKey(10) & 0xFF
        if k ==27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

        
    


show_Video()


