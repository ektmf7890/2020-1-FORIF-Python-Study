#QCheckBox_1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("QCheckBox_1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox.stateChanged.connect(self.chkFunc)  #stateChanged 시그널 
        self.checkBox_2.stateChanged.connect(self.chkFunc)
        self.checkBox_3.stateChanged.connect(self.chkFunc)

        self.label.setText("Vacation to Korea!")  #Display-QLabel 위젯 
        
        
    def chkFunc(self):
        if self.checkBox.isChecked(): print("부산 Checked")  #isChecked()로 확
        if self.checkBox_2.isChecked(): print("제주도 Checked")
        if self.checkBox_3.isChecked(): print("서울 Checked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()































    
