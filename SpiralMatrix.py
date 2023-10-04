n = int(input())
array = [[0 for j in range(n)] for i in range(n)]
num = 1
for i in range(n):
    array[0][i] = num
    num += 1
i = 0
nSquare = n * n
while num < nSquare:
    n = n - 1
    for j in range(n-i):
        array[j+1+i][n] = num
        num += 1
    for k in range(n-1-i, -1, -1):
        array[n][k+i] = num
        num += 1
    for t in range(n-i, 1, -1):
        array[t-1+i][i] = num
        num += 1
    for m in range(n-1-i):
        array[i+1][m+1+i] = num
        num += 1
    i = i + 1
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=" ")
    print()