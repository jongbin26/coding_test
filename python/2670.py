n = int(input())
dp = list(float(input()) for _ in range(NotImplemented))
for i in range(1, n):
    dp[i] = max(dp[i], dp[i] * dp[i - 1])
print('%0.3f' % max(dp))
