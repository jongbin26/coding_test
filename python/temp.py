n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
ans = []
dp = [[0] * n for _ in range(n)]
dp[0][0] = array[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + array[0][i]
    dp[i][0] = dp[i-1][0] + array[i][0]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + array[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 -1
    
    
    if x1 == 0 and y1 != 0:
        ans.append(dp[x2][y2] - dp[x2][y1-1])
    elif x1 != 0 and y1 == 0:
        ans.append(dp[x2][y2] - dp[x1-1][y2])
    elif x1 == 0 and y1 == 0:
        ans.append(dp[x2][y2])
    else:
        ans.append(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
[print(i) for i in ans]