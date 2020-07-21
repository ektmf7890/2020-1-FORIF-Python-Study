#QComboBox_1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("QComboBox_1.ui")[0]

class WindowClass (QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.syncComboBox()  #2개의 콤보박스를 동기화시키는 코드

        #function to comboBox1 (currenIndexChanged signal)
        self.comboBox_1.currentIndexChanged.connect(self.displayLabelFunc)

        #function to buttons
        self.printButton.clicked.connect(self.printFunc)
        self.clearButton.clicked.connect(self.clearFunc)
        self.addButton.clicked.connect(self.addFunc)
        self.deleteButton.clicked.connect(self.deleteFunc)

        #function to lineEdit
        self.addLine.returnPressed.connect(self.addFunc)
        

    def syncComboBox(self):
        for i in range(0, self.comboBox_1.count()):
            self.comboBox_2.addItem(self.comboBox_1.itemText(i))
        
    def displayLabelFunc(self):
        self.displayLabel.setText(self.comboBox_1.currentText())

    def printFunc(self):
        print(self.comboBox_1.currentText())

    def clearFunc(self):
        self.comboBox_1.clear()
        self.comboBox_2.clear()

    def addFunc(self):
        self.item = self.addLine.text()

        self.comboBox_1.addItem(self.item)
        self.comboBox_2.addItem(self.item)
        print(f"\"{self.item}\" is added to list.")
        
    def deleteFunc(self):
        self.index = self.comboBox_2.currentIndex()
        self.item_2 = self.comboBox_2.currentText()
        
        self.comboBox_1.removeItem(self.index)
        self.comboBox_2.removeItem(self.index)
        
        print(f"\"{self.item_2}\" is deleted from list.")

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
        



























        
