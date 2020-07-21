#class_ex1.py

#슈퍼 마리오 클래스
class SuperMario:
    def __init__(self):  #클래스의 속성들을 초기화시켜주는 init 메서드
        self.health = int(input('체력 : '))
        self.coin = 0
        print('현재 체력 : ', self.health)
        print('현재 코인 : ', self.coin)
        print('\n')
        
    def fight(self):  #싸울 때마다 체력을 1씩 감소시키는 메서드
        self. health = self.health - 1
        print('남은 체력 : ', self.health, end = '\n\n')

    def got_coin(self):  #코인을 먹으면 coin 속성을 1씩 증가시키는 메서드
        self.coin = self.coin + 1
        print('남은 코인 : ', self.coin, end = '\n\n')

#SuperMario 클래스의 인스턴스 생성
myMario = SuperMario()
#생성한 인스턴스로 클래스이 메서드를 호출해 사용해봅시다.
myMario.fight()
myMario.got_coin()


















