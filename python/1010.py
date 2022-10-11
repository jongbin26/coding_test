import math
n = int(input())
ans = []
for _ in range(n):
    k, n = map(int, input().split())
    tmp = math.comb(n, k)
    ans.append(tmp)
    
for i in ans:
    print(i)