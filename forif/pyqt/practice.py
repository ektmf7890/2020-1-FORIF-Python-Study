#practice.py

import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5.QtGui import *

form_class = uic.loadUiType("practice.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.te1.textChanged.connect(self.te1_changed)

    def te1_changed(self):
        self.statusBar().showMessage(self.te1.toPlainText())

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    


        
