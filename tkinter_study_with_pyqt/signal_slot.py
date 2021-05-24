from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal
from PIL import Image
import os
import time

class initial_signal():



    def __init__(self,mainform):
        self.main_form = mainform                                                           # main form field
        self.main_form.btn_File_add.clicked.connect(self.show_file_dialog)                  # 파일 불러오기 Dialog open
        self.main_form.btn_Close_app.clicked.connect(mainform.close)                        # main window close
        self.main_form.btn_List_discard.clicked.connect(self.list_discard)
        self.main_form.btn_Start_conversion.clicked.connect(self.conversion_start)
        self.main_form.btn_Find_filepath.clicked.connect(self.file_save_path)
        

    
    #### slot
    
    ## File Dialog pop up
    def show_file_dialog(self): 
        frame = QFileDialog.getOpenFileNames(self.main_form,"open choose file","pygame_study",filter="*.png")
        for path in frame[0]:
            self.main_form.listw_File_list.addItem(path)

    
    ## list widget item discard
    def list_discard(self):
        item_name = self.main_form.listw_File_list.selectedItems()
        for i in item_name:
            print(i.text())


        lst_item = []
        item_row = self.main_form.listw_File_list.selectedIndexes()
        for i in item_row:
            lst_item.append(i.row())

        lst_item.sort()
        lst_item.reverse()

        for i in lst_item:
            self.main_form.listw_File_list.takeItem(i)

        
    def file_save_path(self):
        frame = QFileDialog.getExistingDirectory(self.main_form,"select directory")
        self.main_form.le_File_path.setText(frame)
    
    ## conversion start
    def conversion_start(self):
        if self.main_form.listw_File_list.count() == 0:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("test")
            msg_box.setText("need to add image file")
            msg_box.exec_()

        else:
            if len(self.main_form.le_File_path.text()) == 0:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("test")
                msg_box.setText("need to add File path")
                msg_box.exec_()

            else:
                self.merge_image()


    

    def merge_image(self):
        images = [Image.open(self.main_form.listw_File_list.item(item_row).text()) for item_row in range(self.main_form.listw_File_list.count())]
        # print(images)
        widths = [x.size[0] for x in images]
        heights = [x.size[1] for x in images]

        max_width , total_height = max(widths), sum(heights)

        # 스케치북 준비
        result_img = Image.new("RGB",(max_width,total_height),(255,255,255))    # 배경 
        x_offset = 0
        y_offset = 0                                                            # y 위치
        for idx,img in enumerate(images):
            x_offset = int((max_width/2) - (img.size[0]/2))
            result_img.paste(img,(x_offset,y_offset))
            y_offset += img.size[1]

            progress = (idx + 1) / len(images) * 100
            self.main_form.pgb_Merge_progress.setValue(progress)
            time.sleep(2)

        dest_path = os.path.join(self.main_form.le_File_path.text(),"merge_photo.jpg")

        result_img.save(dest_path)

        msg_box = QMessageBox()
        msg_box.setWindowTitle("merge_image")
        msg_box.setText("complete")
        msg_box.exec_()
    




    
    

    
    
        