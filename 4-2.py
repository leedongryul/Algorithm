N = input()
move_types = ['a','b','c','d','e','f','g','h']
dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]          #오, 왼, 위, 아래 순
count = 0

for i in range(len(move_types)):
    if move_types[i] in N:
        x = i+1

for j in range(1,9):
    if str(j) in N:
        y = j               #x,y로 위치 초기화
        y = int(y)

for i in range(0,8):
    nx = x + dx[i]
    ny = y + dy[i]
    print(ny, nx)
    if nx >= 1 and ny >= 1 and nx < 9 and ny < 9:
        count += 1

print(count)