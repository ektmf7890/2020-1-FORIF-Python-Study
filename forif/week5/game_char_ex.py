#game_char-ex.py

class Knight:
    def __init__(self, health, mana, ap):
        self.health = health
        self.mana = mana
        self.ap = ap
    def tibbers(self):
        print('Tibber : Damage {0}' .format((self.ap*0.65) + 400))

health, mana, ap = map(float, input('체력, 마나, AP : ').split())
my_knight = Knight(health=health, mana = mana, ap = ap)



















