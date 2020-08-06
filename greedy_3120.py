a,b = map(int, input().split())
res = b-a
count = 0
while abs(res):
    if abs(res) >=8:
        if res >=8:
            res-=10
        elif res <= -8:
            res+=10
    elif abs(res) <= 7 & abs(res) >= 3:
        if res >= -7 & res <=-3:
            res +=5
        elif res <= 7 & res >=3:
            res -=5
    else:
        if res < 0:
            res += 1
        else:
            res -= 1
    count+=1

print(count)
