Выведите таблицу размером  n × n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь  n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9



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
