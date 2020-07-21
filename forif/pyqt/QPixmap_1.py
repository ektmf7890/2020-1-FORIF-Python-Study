#QPixmap_1.py
import sys
import urllib.request
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,400,900,900)

        #Getting image from WEB and saing it as object
        urlString ="https://avatars1.githubusercontent.com/u/44885477?s=460&v=4"
        imageFromWeb = urllib.request.urlopen(urlString).read()

        #Loading imabe from web into QPixmap object
        self.qpixmapvar = QPixmap()
        self.qpixmapvar.loadFromData(imageFromWeb)
        self.qpixmapvar = self.qpixmapvar.scaledToWidth(400)

        self.pixmap_label = QLabel(" ", self)
        self.pixmap_label.move(10,10)
        self.pixmap_label.resize= (800,800)
        self.pixmap_label.setPixmap(self.qpixmapvar)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()
        

