#info_view.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.QtGui import *
from PyQt5 import uic
from option_car_rent import CarRentWindow

infoview_class = uic.loadUiType("c:/python_study/qtproject1/ui_files/infoview.ui")[0]

class InfoView(QDialog, infoview_class):
    def __init__(self, choice, wishList):
        super().__init__()
        self.setupUi(self)

        if choice == 1:
            self.setWindowTitle("Forif 여행사와 행복한 국내여행을 계획해 보아요!")
            self.location_box.addItem("서울")
            self.location_box.addItem("부산")
            self.location_box.addItem("제주도")
            
        if choice == 2:
            self.setWindowTitle("Forif 여행사와 행복한 유럽 여행을 계획해 보아요!")
            self.location_box.addItem("영국")
            self.location_box.addItem("스페인")
            self.location_box.addItem("스위스")
        
        if choice == 3:
            self.setWindowTitle("Forif 여행사와 행복한 동남아 여행을 계획해 보아요!")
            self.location_box.addItem("라오스")
            self.location_box.addItem("필리핀")
            self.location_box.addItem("베트남")
            
        #요것조것 설정해주기
        self.adult_line.setText(f"성인 {self.adult_spinBox.value()}명")
        self.child_line.setText(f"어린이 {self.child_spinBox.value()}명")
        #여행지 : QComboBox
        self.location_box.activated.connect(self.locationBoxChanged)
        #여행기간 : QDateEdit
        self.startDate.dateChanged.connect(lambda state, date=self.startDate : self.dateChanged(state, date))
        self.endDate.dateChanged.connect(lambda state, date=self.endDate : self.dateChanged(state, date))
        #여행 인원 : QSpinBox
        self.adult_spinBox.valueChanged.connect(lambda state, spinBox=self.adult_spinBox : self.spinBoxChanged(state, spinBox))
        self.child_spinBox.valueChanged.connect(lambda state, spinBox=self.child_spinBox : self.spinBoxChanged(state, spinBox))
        #wishlist에 추가 : QPushButton
        self.wishlist_btn.clicked.connect(lambda state, wishlist = wishList : self.addToWishList(state, wishlist))

        #option 추가
        self.option_list = [0, 0, 0]
        self.carRent_btn.clicked.connect(self.onCarRentBtnClicked)
        
    def locationBoxChanged(self):
        self.location_line.setText(self.location_box.currentText())

    def dateChanged(self, state, date):
        if date == self.startDate:
            self.startdate_line.setText(date.date().toString("yyyy-MM-dd"))
        elif date == self.endDate:
            self.enddate_line.setText(date.date().toString("yyyy-MM-dd"))

    def spinBoxChanged(self, state, spinBox):
        if spinBox == self.adult_spinBox:
            self.adult_line.setText(f"성인 {spinBox.value()}명")
        elif spinBox == self.child_spinBox:
            self.child_line.setText(f"어린이 {spinBox.value()}명")
            
    def addToWishList(self, state, wishlist):
        info = {"destination":self.location_line.text(), "startDate":self.startdate_line.text(), "endDate":self.enddate_line.text(),
                "adult":int(self.adult_spinBox.value()), "child":int(self.child_spinBox.value()), "optionList":self.option_list}
        ans = QMessageBox.question(self,"Add to wishlist", "위시리스트에 추가하시겠습니까?", QMessageBox.Yes|QMessageBox.No,
                          QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            wishlist.append(info)
            self.close()

    def onCarRentBtnClicked(self):
        car_window = CarRentWindow(self.option_list)

        car_window.show()
        car_window.exec()
        
        if self.option_list[0]=="sonata":
            self.carRent_line.setText("쏘나타 뉴라이즈 (1일 24,000원)")
        elif self.option_list[0]=="genesis":
            self.carRent_line.setText("제네시스 EQ900 (1일 90,000원)")
        elif self.option_list[0]=="thenewgrand":
            self.carRent_line.setText("더 뉴 그랜드 (1일 40,000원)")
        elif self.option_list[0]==0:
            self.carRent_line.setText("미포함")

    
            
        
        

            
