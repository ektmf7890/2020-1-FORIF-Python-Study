#dojang_unit35.py

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        if hour <= 24 and minute <= 60 and second <= 60: return True
        else: return False
        
   
    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time_instance = cls(hour,minute,second)
        return time_instance



time_string = input('시간을 입력하세요 : ')

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print('시 : {0}\n분 : {1}\n초 : {2}'.format(t.hour, t.minute, t.second))
else:
    print('잘못된 시간 형식입니다.')































        



















        
