#QSliderQDial_1.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("QSliderQDial1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Vertical Slider
        self.verticalSlider.sliderMoved.connect(self.verticalSliderMoved)
        self.verticalSlider.valueChanged.connect(self.verticalSliderMoved)
        self.btn_vinfo.clicked.connect(self.btnVInfoClicked)
        
        
        #Horizontal slider
        self.horizontalSlider.sliderMoved.connect(self.horizontalSliderMoved)
        self.horizontalSlider.valueChanged.connect(self.horizontalSliderMoved)
        self.btn_hinfo.clicked.connect(self.btnHInfoClicked)
        
        
        #Dial
        self.dial.sliderMoved.connect(self.dialSliderMoved)
        self.dial.valueChanged.connect(self.dialSliderMoved)
        self.btn_dinfo.clicked.connect(self.btnDInfoClicked)
        

    def verticalSliderMoved(self):
        self.label_vertical.setText(str(self.verticalSlider.value()))
        
    def horizontalSliderMoved(self):
        self.label_horizontal.setText(str(self.horizontalSlider.value()))
        
    def dialSliderMoved(self):
        self.label_dial.setText(str(self.dial.value()))

    def btnVInfoClicked(self):
        print("Vertical Slider Info".center(30,"-"))
        print(f"Minimum : {self.verticalSlider.minimum()}")
        print(f"Maximum : {self.verticalSlider.maximum()}")
        print(f"Single Step : {self.verticalSlider.singleStep()}")
        print(f"Page Step : {self.verticalSlider.pageStep()}")

    def btnHInfoClicked(self):
        print("Horizontal Slider Info".center(30,"-"))
        print(f"Minimum : {self.horizontalSlider.minimum()}")
        print(f"Maximum : {self.horizontalSlider.maximum()}")
        print(f"Single Step : {self.horizontalSlider.singleStep()}")
        print(f"Page Step : {self.horizontalSlider.pageStep()}")

    def btnDInfoClicked(self):
        print("Dial Info".center(30,"-"))
        print(f"Minimum : {self.dial.minimum()}")
        print(f"Maximum : {self.dial.maximum()}")
        print(f"Single Step : {self.dial.singleStep()}")
        print(f"Page Step : {self.dial.pageStep()}")
        


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()
    


















