import sys
import os
from PyQt5.QtWidgets import QApplication , QMainWindow , QAction
from PyQt5.QtGui import QIcon

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")

class MyApp(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        
        exitAction = QAction(QIcon(os.path.join(image_folder_path,"icon.png")),"Exit",self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(QApplication.quit)

        self.statusBar()

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        



        # 초기화 기본

        self.setWindowTitle("Menu bar")
        self.setGeometry(300,300,400,200)                   # 화면 위치 , 크기 설정
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    