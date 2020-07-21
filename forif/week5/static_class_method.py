#static_class_method.py

class Date:
    #날짜 형식이 올바른지 확인하는 정적 메서드
    @staticmethod
    def is_date_valid(date):
        year, month, day = map(int, date.split('-'))
        if month <= 12 and day <= 31:
            return True
        else: return False


date_value =  input('날짜를 입력하세요 : ')

if Date.is_date_valid(date_value):
    print('올바른 날짜 형식')
else:
    print('잘못된 날짜 형식')
