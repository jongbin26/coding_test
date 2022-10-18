n, k = map(int, input().split())
arr = [[0,0]]
dp = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(1, n+1):	#물건
    for j in range(1, k+1):	#무게
        dp[i][j] = dp[i-1][j]
        if arr[i][0] <= j:
            dp[i][j] = max(arr[i][1] + dp[i-1][j-arr[i][0]], dp[i-1][j])
print(max(dp[n]))