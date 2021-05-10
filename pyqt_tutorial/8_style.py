import sys
import os
from PyQt5.QtWidgets import QApplication , QMainWindow , QWidget, QLabel , QVBoxLayout , QDesktopWidget
from PyQt5.QtCore import QDate

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")


class MyApp(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):

        lbl_Red = QLabel("Red")
        lbl_Green = QLabel("Green")
        lbl_Blue = QLabel("Blue")

        lbl_Red.setStyleSheet("color : red;"
                            "border-style : solid;"
                            "border-width : 2px;"
                            "border-color : #FA8072;"
                            "border-radius : 3px")

        lbl_Green.setStyleSheet("color : green;"
                            "border-style : solid;"
                            "border-width : 2px;"
                            "border-color : #FA8072;"
                            "border-radius : 3px")
        
        lbl_Blue.setStyleSheet("color : blue;"
                            "border-style : solid;"
                            "border-width : 2px;"
                            "border-color : #FA8072;"
                            "border-radius : 3px")

        vbox = QVBoxLayout()
        
        vbox.addWidget(lbl_Red)
        vbox.addWidget(lbl_Green)
        vbox.addWidget(lbl_Blue)

        self.setLayout(vbox)


        self.setWindowTitle("Style")
        self.resize(500,350)                # 화면 위치 , 크기 설정
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    