T = int(input())
ans = []
for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * (k+1) for _ in range(k+1)]
    s = [0] * (k+1)
    for i in range(1, k+1):
        s[i] = s[i-1] + arr[i-1]
    
    for i in range(2, k+1):
        for j in range(1, k+2-i):
            dp[j][j+i-1] = min([dp[j][j+a] + dp[j+a+1][j+i-1] for a in range(i-1)]) + s[j+i-1] - s[j-1]
    ans.append(dp[1][k])
print(*ans, sep='\n')