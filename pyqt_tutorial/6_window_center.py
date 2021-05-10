import sys
import os
from PyQt5.QtWidgets import QApplication , QMainWindow , QWidget, QDesktopWidget

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")

class MyApp(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Menu bar")
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
    