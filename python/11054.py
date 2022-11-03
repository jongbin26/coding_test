n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

#increase
for i in range(n):
    high = 0
    for j in range(0, i):
        if arr[j] < arr[i]:
            high = max(high, dp[j])
    dp[i] = high + 1
    
#decrease
for i in range(n):
    high = 0
    for j in range(0, i):
        if arr[j] > arr[i]:
            high = max(high, dp[j])
    dp[i] = max(dp[i], high + 1)
    
print(max(dp))