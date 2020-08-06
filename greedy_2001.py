res1 = 2001
res2 = 2001

for i in range(3):
    a = int(input())
    res1 = min(a,res1)

for j in range(2):
    a = int(input())
    res2 = min(a, res2)

print(round((res1+res2)*1.1,2))