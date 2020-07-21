import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic

log_class = uic.loadUiType('C:/python_study/qtproject2/log.ui')[0]
record_class = uic.loadUiType('C:/python_study/qtproject2/record.ui')[0]
main_class = uic.loadUiType('C:/python_study/qtproject2/main.ui')[0]

day1 = []
day2 = []
day3 = []

start_date = QDate.currentDate()

class Log(QDialog, log_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("운동 로그 조회")
        self.date_edit.setDate(start_date)
        self.date_edit.setDateRange(start_date, start_date.addDays(2))
        global day1

        if day1:
            log_count = 0
            for log in day1:
                self.log_table.insertRow(log_count)
                self.log_table.setItem(log_count, 0, QTableWidgetItem(log.get("date").toString("yyyy-MMM-dd")))
                self.log_table.setItem(log_count, 1, QTableWidgetItem(log.get("category")))
                self.log_table.setItem(log_count, 2, QTableWidgetItem(str(log.get("time"))+"분"))
                chk_box = QCheckBox("인증하기")
                self.log_table.setCellWidget(log_count, 3, chk_box)
                log_count += 1                
        else:
            self.info_label.setText("*선택 날짜에 해당하는 운동 로그가 없습니다.*")
            
        self.date_edit.dateChanged.connect(self.addToTable)

    def addToTable(self):
        global day1, day2, day3

        for i in range(self.log_table.rowCount()):
            self.log_table.removeRow(0)
        
        if self.date_edit.date() == start_date:
            choosed_day = day1
        elif self.date_edit.date() == start_date.addDays(1):
            choosed_day = day2
        else:
            choosed_day = day3
            
        if choosed_day:
            log_count = 0
            for log in choosed_day:
                self.log_table.insertRow(log_count)
                self.log_table.setItem(log_count, 0, QTableWidgetItem(log.get("date").toString("yyyy-MMM-dd")))
                self.log_table.setItem(log_count, 1, QTableWidgetItem(log.get("category")))
                self.log_table.setItem(log_count, 2, QTableWidgetItem(str(log.get("time"))+"분"))
                chk_box = QCheckBox()
                self.log_table.setCellWidget(log_count, 3, chk_box)
                log_count += 1
        else:
            self.info_label.setText("*선택 날짜에 해당하는 운동 로그가 없습니다.*")

        

class Record(QDialog, record_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("운동 계획 기록하기")

        #선택할 수 있는 날짜의 범위를 시작일 부터 3일로 제한하기
        self.date_edit.setDate(start_date)
        self.date_edit.setDateRange(start_date, start_date.addDays(2))

        self.record_btn.clicked.connect(self.recordLog)

    def recordLog(self):
        global day1, day2, day3
        
        new_log = {"category":self.category.currentText(), "date":self.date_edit.date(),
                   "time":self.time.value()}
        if new_log.get("date") == start_date:
            day1.append(new_log)
        elif new_log.get("date") == start_date.addDays(1):
            day2.append(new_log)
        else:
            day3.append(new_log)
            
        ans = QMessageBox.question(self, "운동 계획 기록 완료!",
                                   "운동 계획이 추가되었습니다.\n운동 계획 로그를 조회하러 가시겠습니까?",
                                   QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.No:
            self.close()
        else:
            self.close()
            log_window = Log()
            log_window.show()
            log_window.exec()
            

    
class Main(QMainWindow, main_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.setWindowTitle("작심삼일 운동 챌린지")
        self.log_action.triggered.connect(self.logBtnClicked)
        
        self.record_btn.clicked.connect(self.recordBtnClicked)
        self.log_btn.clicked.connect(self.logBtnClicked)
        
    def recordBtnClicked(self):
        record_window = Record()
        record_window.show()
        record_window.exec()

    def logBtnClicked(self):
        log_window = Log()
        log_window.show()
        log_window.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
