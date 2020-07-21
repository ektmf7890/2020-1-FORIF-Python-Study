#week2-adv1.py
#코딩도장23장 심사문제

col, row = map(int,input().split())

def adj(i,j, matrix):
    border = []
    for a in [i-1, i , i+1]:
        for b in [j-1, j, j+1]:
            if (a>=0 and a<row) and (b>=0 and b<col):
                border.append(matrix[a][b])
    return border.count('*')
                
matrix = []
for i in range(row):
    matrix.append(list(input()))


for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            count = adj(i,j,matrix)
            matrix[i][j] = count
        print(matrix[i][j], end='')
    print()
    




















