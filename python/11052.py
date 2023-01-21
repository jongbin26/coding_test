n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = arr[i-1]
for i in range(2, n+1):
    devide = i // 2
    max_val = 0
    for j in range(1, devide+1):
        max_val = max(max_val, dp[j] + dp[i-j], arr[i-1])
    dp[i] = max_val
print(dp[n])