import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import signal_slot
import main_form_init


folder_path = os.path.dirname(os.path.abspath(__file__))

form_class = uic.loadUiType(os.path.join(folder_path,"form/main_form.ui"))[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    # module insternce create
    refresh_form = main_form_init.mainform_init()


    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.refresh_form.refresh_screen(self)
        self.sig_slot = signal_slot.initial_signal(self)



if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()