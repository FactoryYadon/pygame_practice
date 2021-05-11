import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic


folder_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(folder_path,"label.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.radioButton.clicked.connect(self.radioButton_clicked)
        self.radioButton_2.clicked.connect(self.radioButton_2_clicked)

        self.cb_1.stateChanged.connect(self.cb_clicked)
        self.cb_2.stateChanged.connect(self.cb_clicked)
        self.cb_3.stateChanged.connect(self.cb_clicked)
        self.cb_4.stateChanged.connect(self.cb_clicked)
        self.gb_cb_1.stateChanged.connect(self.gb_cb_clicked)
        self.gb_cb_2.stateChanged.connect(self.gb_cb_clicked)
        self.gb_cb_3.stateChanged.connect(self.gb_cb_clicked)
        self.gb_cb_4.stateChanged.connect(self.gb_cb_clicked)

    def cb_clicked(self):
        if self.cb_1.isChecked() : print("cb_1 checked")
        if self.cb_2.isChecked() : print("cb_2 checked")
        if self.cb_3.isChecked() : print("cb_3 checked")
        if self.cb_4.isChecked() : print("cb_4 checked")

    def gb_cb_clicked(self):
        if self.gb_cb_1.isChecked() : print("gb_cb_1 checked")
        if self.gb_cb_2.isChecked() : print("gb_cb_2 checked")
        if self.gb_cb_3.isChecked() : print("gb_cb_3 checked")
        if self.gb_cb_4.isChecked() : print("gb_cb_4 checked")


    def radioButton_clicked(self):
        print("btn4 clicked")

    def radioButton_2_clicked(self):
        print("radioButton2 clicked")


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()