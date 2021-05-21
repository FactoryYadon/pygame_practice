import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import signal_slot


folder_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(folder_path,"form/main_form.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        sig_slot = signal_slot.initial_signal(self)

    
    # 이벤트 정리 쪽
    
    def show_file_dialog(self):
        frame = QFileDialog.getOpenFileName(self,"open choose file","pygame_practice",filter="*.png")
        print(frame[0])
        self.tb_File_list.append(frame[0])


    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()