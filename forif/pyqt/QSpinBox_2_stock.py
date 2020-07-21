#QSpinBox_2_stock.py
import sys
from PyQt5.QtWidgets import *

class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200,400,300)

        self.label = QLabel("매도수량 : ",self)
        self.label.move(20,20)

        self.spinBox = QSpinBox(self)
        self.spinBox.move(100,25)
        self.spinBox.resize(80,22)
        
        self.spinBox.setValue(10)
        self.spinBox.setRange(0, 10000)
        self.spinBox.setSingleStep(10)
        self.spinBox.valueChanged.connect(self.spinBoxChanged)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def spinBoxChanged(self):
        val = self.spinBox.value()
        msg = "%d주를 매입합니다."%(val)
        self.statusBar.showMessage(msg)
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
