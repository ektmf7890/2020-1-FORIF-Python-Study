#QPushButton_1.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

#UI파일 연결(같은 디렉토리에 위치)
form_class = uic.loadUiType("QPushButton_1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("우리의 뽀시래기 첫 gui")

        #close button
        self.btn1.clicked.connect(QCoreApplication.instance().quit)
        #status bar
        self.statusBar().showMessage("this is a status bar.")
        #QAction 생성
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(qApp.quit)
        #menu bar
        menubar = self.menuBar()
        file_menu  = menubar.addMenu("&File")
        file_menu.addAction(exit_action)
        edit_menu = menubar.addMenu("&Edit")

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self,"Quit", "Are you sure to quit?",
                             QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.No:
            QCloseEvent.accept()
        else:
            QCoseEvent.ignore()

        
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
    
    















    
