from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
import main_project

class initial_signal(QObject):

    dialog_signal = pyqtSignal(object)

    def __init__(self,mainform):
        super().__init__()
        mainform.btn_File_add.clicked.connect(self.show_file_dialog_emit)            # 파일 불러오기 Dialog open
        mainform.btn_Close_app.clicked.connect(mainform.close)                      # main window close
        self.main_form_inst = mainform
        self.dialog_signal.connect(self.show_file_dialog)
    
    def show_file_dialog(self,form):
        frame = QFileDialog.getOpenFileName(form,"open choose file","pygame_practice",filter="*.png")
        print(frame[0])
        form.tb_File_list.append(frame[0])
    

    def show_file_dialog_emit(self):
        self.dialog_signal.emit(self.main_form_inst)

    




    
    

    
    
        