n = int(input())
move = input().split()
x,y = 1,1

for i in move:
    if i == 'U':
        if x>1:
            x -= 1
    elif i == 'D':
        if x < 5:
            x += 1
    elif i == 'R':
        if y < 5:
            y += 1
    elif i == 'L':
        if y>1:
            y -=1

print(x,y)