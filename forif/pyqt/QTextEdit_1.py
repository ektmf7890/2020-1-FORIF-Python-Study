#QTextEdit_1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont, QColor
#colorVar = QColor(R, G, B, 투명도) 0~255
#fontVar = QFont(FontName, size)

form_class  = uic.loadUiType("QTextEdit_1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10     #윈도우의 텍스트 크기를 10으로 지정 

        self.print_btn.clicked.connect(self.printTextFunc)
        self.clear_btn.clicked.connect(self.clearTextFunc)
        
        self.font_btn.clicked.connect(self.setFontFunc)
        self.italic_btn.clicked.connect(self.setItalicFunc)
        self.red_btn.clicked.connect(self.setRedFunc)
        
        self.size_up_btn.clicked.connect(self.sizeUpFunc)
        self.size_down_btn.clicked.connect(self.sizeDownFunc)
        

    def printTextFunc(self):
        print(self.textEdit.toPlainText())

    def clearTextFunc(self):
        self.textEdit.clear()

    def setFontFunc(self):
        fontVar = QFont("Elephant", self.fontSize)
        self.textEdit.setCurrentFont(fontVar)
        
    def setItalicFunc(self):
        self.textEdit.setFontItalic(True)

    def setRedFunc(self):
        colorVar = QColor(255,0,0)
        self.textEdit.setTextColor(colorVar)

    def sizeUpFunc(self):
        self.fontSize += 1
        self.textEdit.setFontPointSize(self.fontSize)
        
    def sizeDownFunc(self):
        self.fontSize -= 1
        self.textEdit.setFontPointSize(self.fontSize)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()






















    
