#week1-1.py

a = int(input("Num1 : "))
b = int(input("Num2 : "))
c = int(input("Num3:  "))
if a>=b :
    if b>=c: #a>b>c
        print(a,">",b,">",c)
    else:
        if a>=c : #a>c>b:
            print(a,">",c,">",b)
        else : #c>a>b
            print(c,">",a,">",b)
else:
    if a>=c : #b>a>c
        print(b,">",a,">",c)
    else:
        if b>=c: #b>c>a
            print(b,">",a,">",c)
        else : #c>b>a
            print(c,">",b,">",a)

if b>a:
    a,b = b,a
if c>a:
    a,c = c,a
if c>b:
    c,b = b,c
print(a,b,c)
    


        



        
