import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

folder_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(folder_path,"ui/modern.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()