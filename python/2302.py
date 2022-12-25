n = int(input())
k = int(input())
vip = [int(input()) for _ in range(k)]
dp = [0] * (n+1)

if n == 1:
    print(1)
    exit()
if 1 in vip or 2 in vip:
    dp[1], dp[2] = 1, 1
else:
    dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    if i in vip:
        dp[i] = dp[i-1]
    else:
        if i-1 in vip:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-2] + dp[i-1]
print(dp[n])