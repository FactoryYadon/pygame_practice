import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic


folder_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(folder_path,"untitled.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        print("btn1 clicked")

    def btn2_clicked(self):
        print("btn2 clicked")


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()