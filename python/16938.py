from itertools import combinations

n, l, r, x = map(int, input().split())
problems = list(map(int, input().split()))
count = 0

for i in range(2,n+1):
    comb = list(combinations(problems,i))
    for j in comb:
        if l <= sum(j) <= r and max(j) - min(j) >= x:
            count+=1
            
print(count)