w,h = map(int, input().split())
arr = [[0 for i in range(h+1)] for j in range(w+1)]
n = int(input())

for i in range(n):
    l,d,x,y = map(int, input().split())
    if d == 0:
        for j in range(l):
            arr[x][y+j] = 1
    if d == 1:
        for k in range(l):
            arr[x+k][y] = 1

for i in range(1,w+1):
    for j in range(1,h+1):
        print(arr[i][j], end = ' ')
    print()
