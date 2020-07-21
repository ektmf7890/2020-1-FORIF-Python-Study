#option_car_rent.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

carRentWindow_class = uic.loadUiType("C:/python_study/qtproject1/ui_files/option_car_rent.ui")[0]


class CarRentWindow(QDialog, carRentWindow_class):
    def __init__(self, option_list):
        super().__init__()
        self.setupUi(self)
        
        self.sonata_btn.setStyleSheet(
            '''QPushButton{image:url(C:/python_study/qtproject1/images/sonata.png); border:0px;}
               QPushButton:hover{image:url(C:/python_study/qtproject1/images/wishlist.png); border:0px;}
            ''')
        self.genesis_btn.setStyleSheet(
            '''QPushButton{image:url(C:/python_study/qtproject1/images/genesis.png); border:0px;}
               QPushButton:hover{image:url(C:/python_study/qtproject1/images/wishlist.png); border:0px;}
            ''')
        self.thenewgrand_btn.setStyleSheet(
            '''QPushButton{image:url(C:/python_study/qtproject1/images/thenewgrand.png); border:0px;}
               QPushButton:hover{image:url(C:/python_study/qtproject1/images/wishlist.png); border:0px;}
            ''')
        self.sonata_btn.clicked.connect(lambda state, optionList=option_list, btn=self.sonata_btn : self.carBtnClicked(state, optionList, btn))
        self.genesis_btn.clicked.connect(lambda state, optionList=option_list, btn=self.genesis_btn : self.carBtnClicked(state, optionList, btn))
        self.thenewgrand_btn.clicked.connect(lambda state, optionList=option_list, btn=self.thenewgrand_btn : self.carBtnClicked(state, optionList, btn))

        self.cancel_btn.clicked.connect(lambda state, optionList = option_list : self.cancelBtnClicked(state, optionList))

    def carBtnClicked(self, state, optionList, btn):
        if btn == self.sonata_btn:
            ans = QMessageBox.question(self, "Sonata","\'쏘나타\'를 선택하겠습니까?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

            if ans == QMessageBox.Yes:
                optionList[0] = "sonata"
                self.close()
                
        elif btn == self.genesis_btn:
            ans = QMessageBox.question(self, "Genesis","\'제네시스 EQ900\'을 선택하겠습니까?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

            if ans == QMessageBox.Yes:
                optionList[0] = "genesis"
                self.close()

        else:
            ans = QMessageBox.question(self, "The New Grand","\'더 뉴 그랜드\'를 선택하겠습니까?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

            if ans == QMessageBox.Yes:
                optionList[0] = "thenewgrand"
                self.close()

    def cancelBtnClicked(self, state, optionList):
        ans = QMessageBox.question(self, "옵션 선택 취소","렌터카 옵션 선택을 취소하시겠습니까?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

        if ans == QMessageBox.Yes:
            optionList[0] = 0
            self.close()
           

if __name__ == "__main__":
    a = [0, 0, 0]
    app = QApplication(sys.argv)
    myWindow = CarRentWindow(a)
    myWindow.show()
    app.exec_()
    



        
