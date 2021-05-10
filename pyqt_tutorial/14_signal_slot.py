import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QVBoxLayout

class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        self.setWindowTitle("Signal and Slot")
        self.setGeometry(300,300,300,300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mywindow()
    ex.show()
    sys.exit(app.exec_())
