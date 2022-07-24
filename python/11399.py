n = int(input())
p = list(map(int, input().split()))

p.sort()
sum = 0
for i in range(1, len(p)+1):
    sum += p[i-1]*(n-i+1)

print(sum)