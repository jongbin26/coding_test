n = int(input())
dp = [0] * (n+1)
data = [list(map(int, input().split())) for _ in range(n)]

#뒤에서부터 dp 풀이
for i in range(n-1, -1, -1):
    if i + data[i][0] <= n:
        dp[i] += max(dp[i+1], dp[i+data[i][0]] + data[i][1])
    else: dp[i] = dp[i+1]
print(dp)

#앞에서부터 dp 풀이
for i in range(n):
    if i + data[i][0] <= n:
        dp[i+data[i][0]] += data[i][1]
        