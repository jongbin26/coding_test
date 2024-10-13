n = int(input())
num = list(map(int, input().split()))

ans, temp = 0, 0
for i in range(n-1, -1, -1):
    temp = max(temp, num[i])
    ans = max(ans, temp-num[i])
print(ans)
