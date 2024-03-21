n = int(input())
m = int(input())
if m:
    broke = list(map(int, input().split()))
else: broke = []
ans = abs(100-n)
for num in range(1000001):
    for j in str(num):
        if int(j) in broke:
            break
    else: ans = min(ans, len(str(num)) + abs(n-num))
print(ans)