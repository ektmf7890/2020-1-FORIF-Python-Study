#BusinessCardClass.py

class BusinessCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("---------------")
        print("Name :", self.name)
        print("Email :",self.email)
        print("Address :", self.addr)
        print("----------------")

