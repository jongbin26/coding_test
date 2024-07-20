n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [0] * (k+1)
for coin in coins:
    if coin <= k:
        dp[coin] += 1
    for i in range(1, k+1):
        if i + coin <= k:
            dp[i+coin] += dp[i]
print(dp[k])