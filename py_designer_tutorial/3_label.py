import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic


folder_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(folder_path,"label.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_2.clicked.connect(self.btn_2_clicked)
        self.pb_1.clicked.connect(self.btn_1_clicked)

        self.g_pb_1.clicked.connect(self.g_pb_1_clicked)
        self.g_pb_2.clicked.connect(self.g_pb_2_clicked)
        self.g_pb_3.clicked.connect(self.g_pb_3_clicked)
        self.g_pb_4.clicked.connect(self.g_pb_4_clicked)


    def btn_1_clicked(self):
        print(self.lb_1.text())

    def btn_2_clicked(self):
        self.lb_1.setText("change text")

    def g_pb_1_clicked(self):
        print(self.textB_1.toPlainText())

    def g_pb_2_clicked(self):
        self.textB_1.setPlainText("1st line")

    def g_pb_3_clicked(self):
        self.textB_1.append("2nd Line")

    def g_pb_4_clicked(self):
        self.textB_1.clear()
        

        






    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()