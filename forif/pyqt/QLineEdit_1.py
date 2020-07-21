#QLineEdit_1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("QLineEdit_1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.textChanged.connect(self.textInputFunc)
        self.lineEdit.returnPressed.connect(self.printTextFunc)
        self.pushButton.clicked.connect(self.changeTextFunc)

    def textInputFunc(self):
        self.label.setText(self.lineEdit.text())

    def printTextFunc(self):
        print(self.lineEdit.text())

    def changeTextFunc(self):
        self.lineEdit.setText("Change Text")


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    






















        
