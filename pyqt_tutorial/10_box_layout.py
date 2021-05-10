import sys
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QHBoxLayout , QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button1",self)
        btn2 = QPushButton("Button2",self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)


        self.setWindowTitle("Box Layout")
        self.setGeometry(300,300,400,200)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())