arr = [50000,10000,5000,1000,500,100,50,10]
count = 0

n = int(input())
for i in arr:
    count += int(n/i)
    n = n%i

print(count)
