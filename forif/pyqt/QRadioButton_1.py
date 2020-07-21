#QRadioButton_1.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class  = uic.loadUiType("QRadioButton_1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.rad_btn1.clicked.connect(self.groupboxRadBtnFunction)
        self.rad_btn2.clicked.connect(self.groupboxRadBtnFunction)
        self.rad_btn3.clicked.connect(self.groupboxRadBtnFunction)

    def  groupboxRadBtnFunction(self):
        if self.rad_btn1.isChecked() : print("RadioButton1 clicked")
        elif self.rad_btn2.isChecked() : print("RadioButton2 clicked")
        elif self.rad_btn3.isChecked() : print("RadioButton3 clicked")

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
