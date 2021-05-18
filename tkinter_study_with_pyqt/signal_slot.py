from PyQt5.QtWidgets import QFileDialog

class initial_signal():

    def __init__(self,mainform):
        mainform.btn_File_add.clicked.connect(self.show_file_dial(mainform))

    def show_file_dial(self,mainform):
        print("안녕하세요")
    




    
    

    
    
        