#recursive_hanoi.py

def hanoi(n, _from, _by, _to):
    if n == 1:
        print(_from, _to)
        return
    hanoi(n-1, _from, _to, _by)
    print(_from, _to)
    hanoi(n-1,_by, _from, _to)

n = 4
hanoi(n, 1,2,3)
