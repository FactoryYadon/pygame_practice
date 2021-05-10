import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QInputDialog

class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Dialog",self)
        btn1.move(30,30)
        btn1.clicked.connect(self.showDialog)

        self.le1 = QLineEdit(self)
        self.le1.move(120,35)

        self.setWindowTitle("QinputDialog")
        self.setGeometry(300,300,300,300)

    def showDialog(self):
        text , ok = QInputDialog.getText(self, "Input Dialog" , "Enter your name : ")

        if ok:
            self.le1.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mywindow()
    ex.show()
    sys.exit(app.exec_())
