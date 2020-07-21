#price_alignment.py
#코딩도장 24장 심사문제2, week2 심화문제제출 후
prices = map(int, input().split(';'))
prices = list(prices)
prices.sort(reverse=True)
result = list(map(str, prices))


for i in result:
    sections = []
    if len(i)%3!=0:
        sections.append(i[0:len(i)%3])
    index = len(i)%3
    while index<len(i):
        sections.append(i[index:index+3])
        index+=3
    i = ','.join(sections)
    print(i.rjust(9))

