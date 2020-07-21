import sys
from datetime import date
from PyQt5.QtWidgets import *
from PyQt5 import uic

table_class = uic.loadUiType('C:/python_study/plan_ex.ui')[0]


class Plan:
    def __init__(self, date, todo, category, start_time, end_time):
        self.date = date
        self.todo = todo
        self.category = category
        self.start_time = start_time
        self.end_time = end_time


class Main(QMainWindow, table_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #planCount, rowCount, plan_list 속성 정의
        self.planCount = 0
        self.rowCount = 0
        self.plan_list = []

        #plan_table 설정
        self.plan_table.setColumnWidth(1, 200)
        self.plan_table.setColumnWidth(4, 100)

        #list에 추가하기
        self.addButton.clicked.connect(self.addToList)

        #오늘의 일정 업데이트하기
        self.updateButton.clicked.connect(self.updateButtonClicked)

    def addToList(self):
        new_plan = Plan(self.date.date(), self.todo.text(), self.plan_category.currentText(), self.start_time.time(), self.end_time.time())
        
        time = new_plan.start_time.toString("AP hh:mm:ss")+'~'+new_plan.end_time.toString("AP hh:mm:ss")
        
        self.plan_list.append(new_plan)
        self.planCount += 1
        self.count_lineEdit.setText(str(self.planCount))

    def updateButtonClicked(self):
        today = date.today().strftime('%Y-%m-%d')
        for plan in self.plan_list:
            if plan.date.toString('yyyy-MM-dd') == today:
                self.plan_table.insertRow(self.rowCount)
                self.rowCount += 1
                time = plan.start_time.toString("AP hh:mm:ss")+'~'+plan.end_time.toString("AP hh:mm:ss")
                self.plan_table.setItem(self.rowCount-1, 0, QTableWidgetItem(plan.date.toString('yyyy-MM-dd')))
                self.plan_table.setItem(self.rowCount-1, 1, QTableWidgetItem(time))
                self.plan_table.setItem(self.rowCount-1, 2, QTableWidgetItem(plan.todo))
                category_btn = QPushButton(f"{plan.category}")
                self.plan_table.setCellWidget(self.rowCount-1, 3, category_btn)
                ckbox = QCheckBox()
                self.plan_table.setCellWidget(self.rowCount-1, 4, ckbox)
             

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    app.exec_()
    
        
