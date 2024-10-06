n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [0] * (k+1)
for coin in coins:
    for i in range(1, k+1):
        if i % coin == 0:
            dp[i] = min(i // coin, dp[i]) if dp[i] else i // coin
        if dp[i] and (i + coin) <= k:
            dp[i+coin] = min(dp[i] + 1, dp[i+coin]) if dp[i+coin] else dp[i] + 1
print(dp[k]) if dp[k] else print(-1)
