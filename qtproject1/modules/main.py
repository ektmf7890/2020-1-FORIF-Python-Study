#Main.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from infoview import InfoView

main_class = uic.loadUiType("c:/python_study/qtproject1/ui_files/main.ui")[0]


class Main(QMainWindow, main_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Forif Tour")

        #wishlist를 Main클래스의 멤버변수로 만들어 보았습니다.
        self.wishList = []
        
        #QAction 생성
        show_wishlist_action = QAction("Wish List",self)
        show_wishlist_action.triggered.connect(self.showWishList)
        
        #QMenuBar
        menubar = self.menuBar()
        wishlist_menu = menubar.addMenu("My Page")
        wishlist_menu.addAction(show_wishlist_action)

        #QPixmap 클래스로 이미지 넣기 
        qpixmap = QPixmap("c:/python_study/qtproject1/images/travel.jpg")
        self.travel_image.setPixmap(qpixmap)

        #QPushButton, Layout
        self.kor_btn.clicked.connect(lambda state, button=self.kor_btn: self.buttonClicked(state, button))
        self.euro_btn.clicked.connect(lambda state, button=self.euro_btn: self.buttonClicked(state, button))
        self.se_asia_btn.clicked.connect(lambda state, button=self.se_asia_btn: self.buttonClicked(state, button))

    def showWishList(self):
        if self.wishList:
            wishlistwindow = WishListWindow(self.wishList)
            wishlistwindow.show()
            wishlistwindow.exec()
        else:
            msg = QMessageBox.information(self, "Wish list is empty", "아직 추가된 위시 리스트가 없습니다.")


    def buttonClicked(self, state, button):
        if button == self.kor_btn:
            choice = 1
        elif button == self.euro_btn:
            choice = 2
        else:
            choice = 3
        infoviewWindow = InfoView(choice, self.wishList)
        infoviewWindow.show()
        infoviewWindow.exec()

        table = QTableWidget

        
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec_())

    

        
