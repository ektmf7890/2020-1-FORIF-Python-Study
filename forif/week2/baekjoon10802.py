#baekjoon10802.py

a,b = map(int, input().split())
total = 0
for i in range(a,b+1):
    if i%3==0:
        total+=1
        continue
    while i:
        k = i%10
        if k==3 or k==6 or k==9:
            total+=1
            break
        i//=10
print(total%20150523)
