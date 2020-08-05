arr = [[0 for i in range(12)] for j in range(12)]

for i in range(1,11):
    a = input().split()
    for j in range(1,11):
        arr[i][j] = int(a[j-1])
        
x,y = 2,2

while True:
    if(arr[x][y] == 2):
        arr[x][y] = 9
        break;
    
    arr[x][y] = 9
    if (arr[x][y+1] != 1):
        if arr[x][y+1] == 2:
            arr[x][y+1] = 9
            break
        y = y+1
        
    else:
        if arr[x+1][y] == 2:
            arr[x+1][y] = 9
            break
        x = x+1
    if(x == 10 or y == 10):
        break

for i in range(1,11):
    for j in range(1,11):
        print(arr[i][j], end = ' ')
    print()
