#week1-3.py
money = int(input("돈 : "))

if money >= 4000:
    sweet = input("달달한 게 땡기시나요?(Y/N) : ")
    if sweet == "Y":
        cream = input("생크림 좋아하시나요?(Y/N) : ")
        if cream == "Y":
            print("\n오레오 프라푸치노")
        else:
            print("\n알로에 스무디")
    else:
        print("\n카페 라떼")
else:
    sweet = input("달달한 게 땡기시나요?(Y/N) : ")
    if sweet == "Y":
        print("\n바닐라 라떼")
    else:
        hot = input("뜨거운 음료가 땡기나요?(Y/N) : ")
        if hot == "Y":
            print("\n녹차")
        else:
            print("\n아이스 아메리카노")
