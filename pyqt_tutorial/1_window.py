import sys
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 버튼 생성
        btn = QPushButton('Quit',self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 초기화 기본
        self.setWindowTitle("PYQT5 tutorial")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setGeometry(300,300,400,200)                   # 화면 위치 , 크기 설정
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    