#class_namespace.py

class Stock:
    market = "kospi"
    
s1 = Stock()
s1.market = "kosdaq"
s2 = Stock()
print(f"s1의 dict : {s1.__dict__}")
print(f"s2의 dict : {s2.__dict__}")
print()
print(f"s1의 market : {s1.market}")
print(f"s2의 market : {s2.market}")
