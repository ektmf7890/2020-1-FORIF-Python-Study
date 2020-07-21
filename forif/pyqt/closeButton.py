#closeButton.py

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20,20)
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
