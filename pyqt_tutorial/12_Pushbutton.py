import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        # btn1 생성
        btn1 = QPushButton("&Button1",self)
        btn1.setCheckable(True)
        btn1.toggle()

        # btn2 생성
        btn2 = QPushButton(self)
        btn2.setText("Button&2")

        # btn3 생성
        btn3 = QPushButton("Button3",self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        self.setLayout(vbox)

        self.setWindowTitle("Q push button")
        self.setGeometry(300,300,300,200)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mywindow()
    ex.show()
    sys.exit(app.exec_())