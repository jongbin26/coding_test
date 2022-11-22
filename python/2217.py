n = int(input())
lope = list(int(input()) for _ in range(n))

lope.sort()
max_weight = 0
for i in range(0, len(lope)):
    max_weight = max(max_weight, (len(lope)-i) * lope[i])
print(max_weight)