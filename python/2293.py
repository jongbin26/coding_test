n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))

dp = [0] * (k+1)

for i in range(1, n+1):
    for j in range(1, k+1):
        if j == coin[i-1]:
            dp[j] += 1
        elif j > coin[i-1]:
            dp[j] += dp[j-coin[i-1]]
print(dp[k])