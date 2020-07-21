#slice_concatenation.py
#코딩도장 11장 심사문제, week2 심화문제 제출 예장
a = input()
b = input()

list_form_a = []
for i in range(1, len(a), 2):
    list_form_a.append(a[i])
    c = ''.join(list_form_a)
list_form_b = []
for i in range(0, len(b), 2):
    list_form_b.append(b[i])
    d = ''.join(list_form_b)
print(c+d)
    
    
