import ctypes
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

folder_path = os.path.dirname(os.path.abspath(__file__))

dll_path = os.path.join(folder_path,"ActUtlType.dll")
mydll = ctypes.CDLL(dll_path)

form_class = uic.loadUiType(os.path.join(folder_path,"main_form.ui"))[0]


class WindowClass(QMainWindow, form_class) :
    

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()