from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal

class initial_signal():



    def __init__(self,mainform):
        mainform.btn_File_add.clicked.connect(mainform.show_file_dialog)            # 파일 불러오기 Dialog open
        mainform.btn_Close_app.clicked.connect(mainform.close)                      # main window close
        
    

    
    




    
    

    
    
        