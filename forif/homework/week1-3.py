#week1-3.py

movie_rank  = ["어벤져스", "쥬라기 공원", "기생충", "옥자", "살인의 추억"]
a,b = input("알고 싶은 영화 순위의 범위를 알려주세요 : ").split()
a = int(a)
b = int(b)
print(movie_rank[a:b+1])
