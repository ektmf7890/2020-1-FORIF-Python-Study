#QPixmap_2.py

import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

form_class = uic.loadUiType("QPixmap_2.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_loadFromFile.clicked.connect(self.loadFromFile)
        self.btn_loadFromWeb.clicked.connect(self.loadFromWeb)
        self.btn_save.clicked.connect(self.save)

    def loadFromFile(self):
        #QPixmap 객체 생성-> 이미지 파일을 객체에 load->label을 이용해 하면 표시
        self.qpixmapvar = QPixmap()
        self.qpixmapvar.load("check.jpg")
        self.qpixmapvar = self.qpixmapvar.scaledToWidth(600)
        self.label_pixmap.setPixmap(self.qpixmapvar)

    def loadFromWeb(self):
        urlString = "http://photo.hankooki.com/newsphoto/v001/2018/12/06/eyoree20181206143240_B_01_C_1.jpg"
        imageFromWeb = urllib.request.urlopen(urlString).read()

        self.qpixmapvar2 = QPixmap()
        self.qpixmapvar2.loadFromData(imageFromWeb)
        #self.qpixmapvar2 = self.qpixmapvar2.scaledToWidth(500)
        self.label_pixmap.setPixmap(self.qpixmapvar2)
        
    def save(self):
        self.qpixmapSaveVar = self.label_pixmap.pixmap()
        self.qpixmapSaveVar.save("Penguin.jpg")


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()











        
    
        
