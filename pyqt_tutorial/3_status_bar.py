import sys
import os
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton , QToolTip , QMainWindow ,QStatusBar
from PyQt5.QtGui import QIcon ,QFont
from PyQt5.QtCore import QCoreApplication

folder_path = os.path.dirname(os.path.abspath(__file__))
image_folder_path = os.path.join(folder_path,"images")

class MyApp(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        # Tool tip
        QToolTip.setFont(QFont("Sanserif",10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        
        # 버튼 생성
        btn = QPushButton('Quit',self)
        btn.setToolTip("This is a <b>Qpushbutton</b> widget")
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 초기화 기본
        

        self.setWindowTitle("PYQT5 tutorial")
        self.statusBar().showMessage("READY")
        self.setWindowIcon(QIcon(os.path.join(image_folder_path,"icon.png")))
        self.setGeometry(300,300,400,200)                   # 화면 위치 , 크기 설정
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    