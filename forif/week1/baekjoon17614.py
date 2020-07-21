#baekjoon17614.py

def count(a):
    a = str(a)
    a = list(a)
    return a.count('3')+a.count('6')+a.count('9')

n = int(input())
total = 0

for i in range(n):
    total += count(i+1)
print(total)

