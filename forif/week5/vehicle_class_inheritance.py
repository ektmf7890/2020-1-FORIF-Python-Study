#vehicle_class_inheritance.py

class Vehicle:
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage

    def daily_mileage_check(self):
        time = int(input("오늘의 주행 시간(시 단위) : "))
        dist = self.speed*(time)
        self.mileage += dist        
        print(f"\n오늘의 주행거리 : {dist}km")
        print(f"총 주행거리 : {self.mileage}km\n")

class Bus(Vehicle):
    def __init__(self, speed, mileage, max_people):
        super().__init__(speed, mileage)
        self.max_people = max_people
        self.passengers = 0

    def ride_on(self, amount):
        for i in range(amount):
            if self.passengers == self.max_people:
                print(f"\n더 이상 좌석이 없습니다. {amount-i}명은 다음 버스를 이용해주세요.", end="")
                break
            self.passengers += 1
            print("삑!", end="")
        print(f"\n잔여 {self.max_people - self.passengers}석\n")

    def get_off(self, amount):
        self.passengers -= amount
        print(f"{amount}명이 하차하였습니다.")
        print(f"잔여 {(self.max_people)-(self.passengers)}석\n")

bus1 = Bus(50, 1800, 30)
bus1.ride_on(18)
bus1.ride_on(20)
bus1.get_off(10)
bus1.get_off(2)
bus1.daily_mileage_check()


        


        
 



    
        

    
