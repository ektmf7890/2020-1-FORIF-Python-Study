#wishlist.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

wishlist_class = uic.loadUiType("C:/python_study/qtproject1/ui_files/wishlist.ui")[0]

class WishListWindow(QMainWindow, wishlist_class):
    def __init__(self, wishList):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("당신의 위시리스트")

            for i in self.wishList:
                print(f"wishlist{i+1}".center(30, "-"))
                print("여행지 :", i.get("destination"))
                print("여행 기간 :", i.get("startDate"), "~", i.get("endDate"))
                print("여행 인원 : 성인 {0}명, 어린이 {1}명".format(i.get("adult"), i.get("child")) )
                for car in i.get("optionList"):
                    if car == "sonata":
                        print("렌터카 옵션 포함 : 쏘나타")
                    if car == "genesis":
                        print("렌터카 옵션 포함 : 제네시스 EQ900")
                    if car == "thenewgrand":
                        print("렌터카 옵션 포함 : 더 뉴 그랜드")
